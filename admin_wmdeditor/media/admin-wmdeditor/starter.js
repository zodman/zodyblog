wmd_options = { autostart: false, output: 'markdown' };    
var wmd_instances = {};

function create_wmdeditor(textfield) {

	if (!Attacklab || !Attacklab.wmd) {
		alert("WMD hasn't finished loading!");
		return;
	}

	var textarea = document.getElementById('id_' + textfield);
	var previewDiv = document.getElementById('id_' + textfield + '_preview');

	var panes = {input:textarea, preview:previewDiv, output:null};
	var previewManager = new Attacklab.wmd.previewManager(panes);
	var editor = new Attacklab.wmd.editor(textarea,previewManager.refresh);

	wmd_instances[textfield] = {ed:editor, pm:previewManager};
}

function destroy_wmdeditor(textfield) {

	var inst = wmd_instances[textfield];

	if (inst) {
		inst.pm.destroy();
		inst.ed.destroy();
	}
}
