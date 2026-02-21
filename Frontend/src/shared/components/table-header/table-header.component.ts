import { CommonModule } from '@angular/common';
import { Component, ContentChild, EventEmitter, Input, Output, TemplateRef } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { InputTextModule } from 'primeng/inputtext';
import { IconFieldModule } from 'primeng/iconfield';
import { InputIconModule } from 'primeng/inputicon';


@Component({
  standalone: true,
  selector: 'app-table-header',
  imports: [InputTextModule, CommonModule, FormsModule,IconFieldModule,InputIconModule],
  templateUrl: './table-header.component.html',
})
export class TableHeaderComponent {

  @Input() tableRef: any;
  @Output() filterFn: EventEmitter<string> = new EventEmitter<string>();
  @ContentChild('actions', { static: true }) actionsTemplate: TemplateRef<any>;
  @ContentChild('leftSide', { static: true }) leftSideTemplate: TemplateRef<any>;
  @ContentChild('rightSide', { static: true }) rightSideTemplate: TemplateRef<any>;

  searchValue = "";

  onFilter() {
    this.filterFn.emit(this.searchValue);
    if(!this.tableRef) return;
    this.tableRef.filterGlobal(this.searchValue, 'contains');
  }

}
