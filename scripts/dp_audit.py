import click
import os
import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from darusselam.engine import ComplianceEngine

console = Console()

@click.command()
@click.argument('path', default='.')
@click.option('--pillars', default='protocol/pillars.yaml', help='Path to pillars definition file')
def main(path, pillars):
    """Darusselam Protokolü (DP-01) Denetim Aracı"""
    
    console.print(Panel.fit(
        "[bold green]Darusselam Protokolü (DP-01) Denetim Başlatılıyor[/bold green]\n"
        "[dim]Hanif Teknoloji Standartları v0.1.0[/dim]",
        border_style="green"
    ))
    
    if not os.path.exists(pillars):
        console.print(f"[red]Hata:[/red] Protokol tanımları bulunamadı: {pillars}")
        sys.exit(1)
        
    engine = ComplianceEngine(pillars)
    
    with console.status("[cyan]Dosyalar taranıyor...[/cyan]"):
        results = engine.scan_directory(path)
        
    summary = results['summary']
    
    # Summary Table
    table = Table(title="Denetim Özeti")
    table.add_column("Metrik", style="cyan")
    table.add_column("Değer", style="magenta")
    
    table.add_row("Taranan Dosya Sayısı", str(summary['total_files_scanned']))
    table.add_row("Tespit Edilen İhlaller", str(summary['violations_found']))
    status_color = "green" if summary['status'].startswith("PASSED") else "red"
    table.add_row("Durum", f"[{status_color}]{summary['status']}[/{status_color}]")
    
    console.print(table)
    
    if results['violations']:
        v_table = Table(title="Tespit Edilen İhlaller")
        v_table.add_column("Pillar", style="yellow")
        v_table.add_column("Dosya", style="blue")
        v_table.add_column("İşaretçi (Marker)", style="red")
        
        for v in results['violations']:
            v_table.add_row(v['pillar'], v['file'], v['marker'])
            
        console.print(v_table)
        
        console.print("\n[bold yellow]Tavsiye:[/bold yellow] Yukarıdaki ihlaller 'Hanif Teknoloji' standartlarına aykırıdır. Lütfen fıtratı ve insan onurunu korumak için gerekli düzenlemeleri yapın.")
    else:
        console.print("\n[bold green]Tebrikler![/bold green] Projeniz Darusselam Protokolü standartlarına uyumlu görünmektedir.")

if __name__ == "__main__":
    main()
