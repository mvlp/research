import { CommonModule } from '@angular/common';
import { Component, ContentChildren, Input } from '@angular/core';
import { DialogService } from 'primeng/dynamicdialog';

type Severity = "primary" | "success" | "danger" | "warn" | "info" | "help";

@Component({
  selector: 'chips',
  standalone: true,
  providers: [DialogService],
  imports: [CommonModule],
  templateUrl: './chips.component.html',
})
export class ChipsComponent {
  @Input() severity: Severity = "primary";
  @Input() class: string;
  @Input() style: { [klass: string]: any };
}
