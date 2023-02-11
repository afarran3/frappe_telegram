frappe.ui.form.on("Notification", {
	onload: function (frm) {
        frm.fields_dict['recipients'].grid.get_field('receiver_by_telegram_user').get_query = function(doc, cdt, cdn) {
			var child = locals[cdt][cdn];
			return {   
				filters:[
					['user', '!=', ""]
				]
			}
		}
	},


	refresh: function (frm) {
        if(frm.is_new()){
            frm.trigger("channel");
        }
	},


	channel: function (frm) {
        frm.events.show_hide_columns(frm, ["receiver_by_telegram_user"], "recipients", frm.doc.channel == "Telegram");
	},


    show_hide_columns: (frm, fields, table, show) => {
        let grid = frm.get_field(table).grid;
        
        for (let field of fields) {
            grid.fields_map[field].hidden = show ? 0 : 1;
        }
        
        grid.visible_columns = undefined;
        grid.setup_visible_columns();
        
        grid.header_row.wrapper.remove();
        delete grid.header_row;
        grid.make_head();
        
        for (let row of grid.grid_rows) {
            if (row.open_form_button) {
                row.open_form_button.parent().remove();
                delete row.open_form_button;
            }
            
            for (let field in row.columns) {
                if (row.columns[field] !== undefined) {
                    // console.log(row.columns[field]);
                    row.columns[field].remove();
                }
            }

            grid.remove_all();
            delete row.columns;
            row.columns = [];
            row.render_row();
        }  
    }   
});
