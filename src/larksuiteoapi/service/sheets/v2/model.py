# -*- coding: UTF-8 -*-
# Code generated by lark suite oapi sdk gen

from typing import List, Dict, Any
from ....utils.dt import to_json_decorator
import attr




@to_json_decorator
@attr.s
class User(object):
    member_type = attr.ib(type=str, default=None, metadata={'json': 'memberType'})
    member_id = attr.ib(type=str, default=None, metadata={'json': 'memberId'})


@to_json_decorator
@attr.s
class Editors(object):
    users = attr.ib(type=List[User], default=None, metadata={'json': 'users'})
    add_editors = attr.ib(type=List[User], default=None, metadata={'json': 'addEditors'})
    del_editors = attr.ib(type=List[User], default=None, metadata={'json': 'delEditors'})


@to_json_decorator
@attr.s
class Source(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})


@to_json_decorator
@attr.s
class Protect(object):
    lock = attr.ib(type=str, default=None, metadata={'json': 'lock'})
    lock_info = attr.ib(type=str, default=None, metadata={'json': 'lockInfo'})
    user_ids = attr.ib(type=List[int], default=None, metadata={'json': 'userIds'})


@to_json_decorator
@attr.s
class Properties(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})
    title = attr.ib(type=str, default=None, metadata={'json': 'title'})
    index = attr.ib(type=int, default=None, metadata={'json': 'index'})
    hidden = attr.ib(type=bool, default=None, metadata={'json': 'hidden'})
    frozen_row_count = attr.ib(type=int, default=None, metadata={'json': 'frozenRowCount'})
    frozen_col_count = attr.ib(type=int, default=None, metadata={'json': 'frozenColCount'})
    protect = attr.ib(type=Protect, default=None, metadata={'json': 'protect'})


@to_json_decorator
@attr.s
class UpdateSheet(object):
    properties = attr.ib(type=Properties, default=None, metadata={'json': 'properties'})


@to_json_decorator
@attr.s
class CopySheetReply(object):
    properties = attr.ib(type=Properties, default=None, metadata={'json': 'properties'})


@to_json_decorator
@attr.s
class AddSheet(object):
    properties = attr.ib(type=Properties, default=None, metadata={'json': 'properties'})


@to_json_decorator
@attr.s
class OptionsResponse(object):
    multiple_values = attr.ib(type=bool, default=None, metadata={'json': 'multipleValues'})
    highlight_valid_data = attr.ib(type=bool, default=None, metadata={'json': 'highlightValidData'})
    color_value_map = attr.ib(type=Dict[str, str], default=None, metadata={'json': 'colorValueMap'})


@to_json_decorator
@attr.s
class DataValidationResponse(object):
    condition_values = attr.ib(type=List[str], default=None, metadata={'json': 'conditionValues'})
    data_validation_id = attr.ib(type=int, default=None, metadata={'json': 'dataValidationId'})
    data_validation_type = attr.ib(type=str, default=None, metadata={'json': 'dataValidationType'})
    options = attr.ib(type=OptionsResponse, default=None, metadata={'json': 'options'})


@to_json_decorator
@attr.s
class Options(object):
    multiple_values = attr.ib(type=bool, default=None, metadata={'json': 'multipleValues'})
    highlight_valid_data = attr.ib(type=bool, default=None, metadata={'json': 'highlightValidData'})
    colors = attr.ib(type=List[str], default=None, metadata={'json': 'colors'})


@to_json_decorator
@attr.s
class DataValidationRequest(object):
    condition_values = attr.ib(type=List[str], default=None, metadata={'json': 'conditionValues'})
    data_validation_id = attr.ib(type=int, default=None, metadata={'json': 'dataValidationId'})
    data_validation_type = attr.ib(type=str, default=None, metadata={'json': 'dataValidationType'})
    options = attr.ib(type=Options, default=None, metadata={'json': 'options'})


@to_json_decorator
@attr.s
class Merge(object):
    start_row_index = attr.ib(type=int, default=None, metadata={'json': 'startRowIndex'})
    start_column_index = attr.ib(type=int, default=None, metadata={'json': 'startColumnIndex'})
    row_count = attr.ib(type=int, default=None, metadata={'json': 'rowCount'})
    column_count = attr.ib(type=int, default=None, metadata={'json': 'columnCount'})


@to_json_decorator
@attr.s
class Font(object):
    bold = attr.ib(type=bool, default=None, metadata={'json': 'bold'})
    italic = attr.ib(type=bool, default=None, metadata={'json': 'italic'})
    font_size = attr.ib(type=str, default=None, metadata={'json': 'fontSize'})
    clean = attr.ib(type=bool, default=None, metadata={'json': 'clean'})


@to_json_decorator
@attr.s
class Style(object):
    font = attr.ib(type=Font, default=None, metadata={'json': 'font'})
    text_decoration = attr.ib(type=int, default=None, metadata={'json': 'textDecoration'})
    formatter = attr.ib(type=str, default=None, metadata={'json': 'formatter'})
    h_align = attr.ib(type=int, default=None, metadata={'json': 'hAlign'})
    v_align = attr.ib(type=int, default=None, metadata={'json': 'vAlign'})
    fore_color = attr.ib(type=str, default=None, metadata={'json': 'foreColor'})
    back_color = attr.ib(type=str, default=None, metadata={'json': 'backColor'})
    border_type = attr.ib(type=str, default=None, metadata={'json': 'borderType'})
    border_color = attr.ib(type=str, default=None, metadata={'json': 'borderColor'})
    clean = attr.ib(type=bool, default=None, metadata={'json': 'clean'})


@to_json_decorator
@attr.s
class AppendStyleBatch(object):
    ranges = attr.ib(type=List[str], default=None, metadata={'json': 'ranges'})
    style = attr.ib(type=Style, default=None, metadata={'json': 'style'})


@to_json_decorator
@attr.s
class AppendStyle(object):
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})
    style = attr.ib(type=Style, default=None, metadata={'json': 'style'})


@to_json_decorator
@attr.s
class Dimension(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})
    major_dimension = attr.ib(type=str, default=None, metadata={'json': 'majorDimension'})
    start_index = attr.ib(type=int, default=None, metadata={'json': 'startIndex'})
    end_index = attr.ib(type=int, default=None, metadata={'json': 'endIndex'})
    length = attr.ib(type=int, default=None, metadata={'json': 'length'})


@to_json_decorator
@attr.s
class ProtectedRangeUpdate(object):
    protect_id = attr.ib(type=str, default=None, metadata={'json': 'protectId'})
    dimension = attr.ib(type=Dimension, default=None, metadata={'json': 'dimension'})
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})
    lock_info = attr.ib(type=str, default=None, metadata={'json': 'lockInfo'})
    editors = attr.ib(type=Editors, default=None, metadata={'json': 'editors'})


@to_json_decorator
@attr.s
class ProtectedRange(object):
    protect_id = attr.ib(type=str, default=None, metadata={'json': 'protectId'})
    dimension = attr.ib(type=Dimension, default=None, metadata={'json': 'dimension'})
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})
    lock_info = attr.ib(type=str, default=None, metadata={'json': 'lockInfo'})
    editors = attr.ib(type=Editors, default=None, metadata={'json': 'editors'})


@to_json_decorator
@attr.s
class AddProtectedDimension(object):
    dimension = attr.ib(type=Dimension, default=None, metadata={'json': 'dimension'})
    editors = attr.ib(type=List[int], default=None, metadata={'json': 'editors'})
    lock_info = attr.ib(type=str, default=None, metadata={'json': 'lockInfo'})
    protect_id = attr.ib(type=str, default=None, metadata={'json': 'protectId'})


@to_json_decorator
@attr.s
class Destination(object):
    title = attr.ib(type=str, default=None, metadata={'json': 'title'})


@to_json_decorator
@attr.s
class CopySheet(object):
    source = attr.ib(type=Source, default=None, metadata={'json': 'source'})
    destination = attr.ib(type=Destination, default=None, metadata={'json': 'destination'})


@to_json_decorator
@attr.s
class DeleteSheetReply(object):
    result = attr.ib(type=bool, default=None, metadata={'json': 'result'})
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})


@to_json_decorator
@attr.s
class Reply(object):
    update_sheet = attr.ib(type=Properties, default=None, metadata={'json': 'updateSheet'})
    add_sheet = attr.ib(type=AddSheet, default=None, metadata={'json': 'addSheet'})
    copy_sheet = attr.ib(type=CopySheetReply, default=None, metadata={'json': 'copySheet'})
    delete_sheet = attr.ib(type=DeleteSheetReply, default=None, metadata={'json': 'deleteSheet'})


@to_json_decorator
@attr.s
class DeleteSheet(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})


@to_json_decorator
@attr.s
class Request(object):
    add_sheet = attr.ib(type=AddSheet, default=None, metadata={'json': 'addSheet'})
    copy_sheet = attr.ib(type=CopySheet, default=None, metadata={'json': 'copySheet'})
    delete_sheet = attr.ib(type=DeleteSheet, default=None, metadata={'json': 'deleteSheet'})
    update_sheet = attr.ib(type=UpdateSheet, default=None, metadata={'json': 'updateSheet'})


@to_json_decorator
@attr.s
class ConditionFormatFont(object):
    bold = attr.ib(type=bool, default=None, metadata={'json': 'bold'})
    italic = attr.ib(type=bool, default=None, metadata={'json': 'italic'})


@to_json_decorator
@attr.s
class ConditionFormatStyle(object):
    font = attr.ib(type=ConditionFormatFont, default=None, metadata={'json': 'font'})
    text_decoration = attr.ib(type=int, default=None, metadata={'json': 'text_decoration'})
    fore_color = attr.ib(type=str, default=None, metadata={'json': 'fore_color'})
    back_color = attr.ib(type=str, default=None, metadata={'json': 'back_color'})


@to_json_decorator
@attr.s
class ConditionFormatAttr(object):
    operator = attr.ib(type=str, default=None, metadata={'json': 'operator'})
    time_period = attr.ib(type=str, default=None, metadata={'json': 'time_period'})
    formula = attr.ib(type=List[str], default=None, metadata={'json': 'formula'})
    text = attr.ib(type=str, default=None, metadata={'json': 'text'})


@to_json_decorator
@attr.s
class ConditionFormat(object):
    cf_id = attr.ib(type=str, default=None, metadata={'json': 'cf_id'})
    ranges = attr.ib(type=List[str], default=None, metadata={'json': 'ranges'})
    rule_type = attr.ib(type=str, default=None, metadata={'json': 'rule_type'})
    attrs = attr.ib(type=List[ConditionFormatAttr], default=None, metadata={'json': 'attrs'})
    style = attr.ib(type=ConditionFormatStyle, default=None, metadata={'json': 'style'})


@to_json_decorator
@attr.s
class SheetConditionFormat(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheet_id'})
    condition_format = attr.ib(type=ConditionFormat, default=None, metadata={'json': 'condition_format'})


@to_json_decorator
@attr.s
class BlockInfo(object):
    block_token = attr.ib(type=str, default=None, metadata={'json': 'blockToken'})
    block_type = attr.ib(type=str, default=None, metadata={'json': 'blockType'})


@to_json_decorator
@attr.s
class Sheet(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})
    title = attr.ib(type=str, default=None, metadata={'json': 'title'})
    index = attr.ib(type=int, default=None, metadata={'json': 'index'})
    row_count = attr.ib(type=int, default=None, metadata={'json': 'rowCount'})
    column_count = attr.ib(type=int, default=None, metadata={'json': 'columnCount'})
    frozen_row_count = attr.ib(type=int, default=None, metadata={'json': 'frozenRowCount'})
    frozen_col_count = attr.ib(type=int, default=None, metadata={'json': 'frozenColCount'})
    merges = attr.ib(type=List[Merge], default=None, metadata={'json': 'merges'})
    protected_range = attr.ib(type=List[ProtectedRange], default=None, metadata={'json': 'protectedRange'})
    block_info = attr.ib(type=BlockInfo, default=None, metadata={'json': 'blockInfo'})


@to_json_decorator
@attr.s
class ConditionFormatResponse(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheet_id'})
    cf_id = attr.ib(type=str, default=None, metadata={'json': 'cf_id'})
    res_code = attr.ib(type=int, default=None, metadata={'json': 'res_code'})
    res_msg = attr.ib(type=str, default=None, metadata={'json': 'res_msg'})


@to_json_decorator
@attr.s
class DataValidationDeleteResult(object):
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})
    msg = attr.ib(type=str, default=None, metadata={'json': 'msg'})
    success = attr.ib(type=bool, default=None, metadata={'json': 'success'})
    updated_cells = attr.ib(type=int, default=None, metadata={'json': 'updatedCells'})


@to_json_decorator
@attr.s
class DataValidationRange(object):
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})
    data_validation_ids = attr.ib(type=List[int], default=None, metadata={'json': 'dataValidationIds'})


@to_json_decorator
@attr.s
class DimensionProperties(object):
    visible = attr.ib(type=bool, default=None, metadata={'json': 'visible'})
    fixed_size = attr.ib(type=int, default=None, metadata={'json': 'fixedSize'})


@to_json_decorator
@attr.s
class MetainfoProperties(object):
    title = attr.ib(type=str, default=None, metadata={'json': 'title'})
    owner_user = attr.ib(type=int, default=None, metadata={'json': 'ownerUser'})
    sheet_count = attr.ib(type=int, default=None, metadata={'json': 'sheetCount'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})


@to_json_decorator
@attr.s
class SheetCfId(object):
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheet_id'})
    cf_id = attr.ib(type=str, default=None, metadata={'json': 'cf_id'})


@to_json_decorator
@attr.s
class SpreadsheetToken(object):
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})


@to_json_decorator
@attr.s
class UpdateResponse(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    updated_range = attr.ib(type=str, default=None, metadata={'json': 'updatedRange'})
    updated_rows = attr.ib(type=int, default=None, metadata={'json': 'updatedRows'})
    updated_columns = attr.ib(type=int, default=None, metadata={'json': 'updatedColumns'})
    updated_cells = attr.ib(type=int, default=None, metadata={'json': 'updatedCells'})


@to_json_decorator
@attr.s
class Updates(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    updated_range = attr.ib(type=str, default=None, metadata={'json': 'updatedRange'})
    updated_rows = attr.ib(type=int, default=None, metadata={'json': 'updatedRows'})
    updated_columns = attr.ib(type=int, default=None, metadata={'json': 'updatedColumns'})
    updated_cells = attr.ib(type=int, default=None, metadata={'json': 'updatedCells'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})


@to_json_decorator
@attr.s
class ValueRange(object):
    major_dimension = attr.ib(type=str, default=None, metadata={'json': 'majorDimension'})
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})
    values = attr.ib(type=List[List[Any]], default=None, metadata={'json': 'values'})



@to_json_decorator
@attr.s
class SpreadsheetsConditionFormatsBatchCreateReqBody(object):
    sheet_condition_formats = attr.ib(type=List[SheetConditionFormat], default=None, metadata={'json': 'sheet_condition_formats'})


@attr.s
class SpreadsheetsConditionFormatsBatchCreateResult(object):
    responses = attr.ib(type=List[ConditionFormatResponse], default=None, metadata={'json': 'responses'})


@to_json_decorator
@attr.s
class SpreadsheetsConditionFormatsBatchDeleteReqBody(object):
    sheet_cf_ids = attr.ib(type=List[SheetCfId], default=None, metadata={'json': 'sheet_cf_ids'})


@attr.s
class SpreadsheetsConditionFormatsBatchDeleteResult(object):
    responses = attr.ib(type=List[ConditionFormatResponse], default=None, metadata={'json': 'responses'})



@attr.s
class SpreadsheetsConditionFormatsBatchGetResult(object):
    sheet_condition_formats = attr.ib(type=List[SheetConditionFormat], default=None, metadata={'json': 'sheet_condition_formats'})


@to_json_decorator
@attr.s
class SpreadsheetsConditionFormatsBatchUpdateReqBody(object):
    sheet_condition_formats = attr.ib(type=List[SheetConditionFormat], default=None, metadata={'json': 'sheet_condition_formats'})


@attr.s
class SpreadsheetsConditionFormatsBatchUpdateResult(object):
    responses = attr.ib(type=List[ConditionFormatResponse], default=None, metadata={'json': 'responses'})


@to_json_decorator
@attr.s
class SpreadsheetsDataValidationCreateReqBody(object):
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})
    data_validation_type = attr.ib(type=str, default=None, metadata={'json': 'dataValidationType'})
    data_validation = attr.ib(type=DataValidationRequest, default=None, metadata={'json': 'dataValidation'})



@to_json_decorator
@attr.s
class SpreadsheetsDataValidationDeleteReqBody(object):
    data_validation_ranges = attr.ib(type=List[DataValidationRange], default=None, metadata={'json': 'dataValidationRanges'})


@attr.s
class SpreadsheetsDataValidationDeleteResult(object):
    range_results = attr.ib(type=List[DataValidationDeleteResult], default=None, metadata={'json': 'rangeResults'})



@attr.s
class SpreadsheetsDataValidationGetResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})
    data_validations = attr.ib(type=List[DataValidationResponse], default=None, metadata={'json': 'dataValidations'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})


@to_json_decorator
@attr.s
class SpreadsheetsDataValidationUpdateReqBody(object):
    data_validation_type = attr.ib(type=str, default=None, metadata={'json': 'dataValidationType'})
    data_validation = attr.ib(type=DataValidationRequest, default=None, metadata={'json': 'dataValidation'})


@attr.s
class SpreadsheetsDataValidationUpdateResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    sheet_id = attr.ib(type=str, default=None, metadata={'json': 'sheetId'})
    data_validation = attr.ib(type=DataValidationResponse, default=None, metadata={'json': 'dataValidation'})


@to_json_decorator
@attr.s
class SpreadsheetsDimensionRangeAddReqBody(object):
    dimension = attr.ib(type=Dimension, default=None, metadata={'json': 'dimension'})


@attr.s
class SpreadsheetsDimensionRangeAddResult(object):
    add_count = attr.ib(type=int, default=None, metadata={'json': 'addCount'})
    major_dimension = attr.ib(type=str, default=None, metadata={'json': 'majorDimension'})


@to_json_decorator
@attr.s
class SpreadsheetsDimensionRangeDeleteReqBody(object):
    dimension = attr.ib(type=Dimension, default=None, metadata={'json': 'dimension'})


@attr.s
class SpreadsheetsDimensionRangeDeleteResult(object):
    del_count = attr.ib(type=int, default=None, metadata={'json': 'delCount'})
    major_dimension = attr.ib(type=str, default=None, metadata={'json': 'majorDimension'})


@to_json_decorator
@attr.s
class SpreadsheetsDimensionRangeUpdateReqBody(object):
    dimension = attr.ib(type=Dimension, default=None, metadata={'json': 'dimension'})
    dimension_properties = attr.ib(type=DimensionProperties, default=None, metadata={'json': 'dimensionProperties'})



@to_json_decorator
@attr.s
class SpreadsheetsImportReqBody(object):
    file = attr.ib(type=List[int], default=None, metadata={'json': 'file'})
    name = attr.ib(type=str, default=None, metadata={'json': 'name'})
    folder_token = attr.ib(type=str, default=None, metadata={'json': 'folderToken'})


@attr.s
class SpreadsheetsImportResult(object):
    ticket = attr.ib(type=str, default=None, metadata={'json': 'ticket'})



@attr.s
class SpreadsheetsImportResultResult(object):
    ticket = attr.ib(type=str, default=None, metadata={'json': 'ticket'})
    url = attr.ib(type=str, default=None, metadata={'json': 'url'})
    warning_code = attr.ib(type=int, default=None, metadata={'json': 'warningCode'})


@to_json_decorator
@attr.s
class SpreadsheetsInsertDimensionRangeReqBody(object):
    dimension = attr.ib(type=Dimension, default=None, metadata={'json': 'dimension'})
    inherit_style = attr.ib(type=str, default=None, metadata={'json': 'inheritStyle'})



@to_json_decorator
@attr.s
class SpreadsheetsMergeCellsReqBody(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})
    merge_type = attr.ib(type=str, default=None, metadata={'json': 'mergeType'})


@attr.s
class SpreadsheetsMergeCellsResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})



@attr.s
class SpreadsheetsMetainfoResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    properties = attr.ib(type=MetainfoProperties, default=None, metadata={'json': 'properties'})
    sheets = attr.ib(type=List[Sheet], default=None, metadata={'json': 'sheets'})


@to_json_decorator
@attr.s
class SpreadsheetsProtectedRangeBatchCreateReqBody(object):
    add_protected_dimension = attr.ib(type=List[AddProtectedDimension], default=None, metadata={'json': 'addProtectedDimension'})


@attr.s
class SpreadsheetsProtectedRangeBatchCreateResult(object):
    add_protected_dimension = attr.ib(type=List[AddProtectedDimension], default=None, metadata={'json': 'addProtectedDimension'})


@to_json_decorator
@attr.s
class SpreadsheetsProtectedRangeBatchDeleteReqBody(object):
    protect_ids = attr.ib(type=List[str], default=None, metadata={'json': 'protectIds'})


@attr.s
class SpreadsheetsProtectedRangeBatchDeleteResult(object):
    del_protect_ids = attr.ib(type=List[str], default=None, metadata={'json': 'delProtectIds'})



@attr.s
class SpreadsheetsProtectedRangeBatchGetResult(object):
    protected_range = attr.ib(type=List[ProtectedRange], default=None, metadata={'json': 'protectedRange'})


@to_json_decorator
@attr.s
class SpreadsheetsProtectedRangeBatchUpdateReqBody(object):
    requests = attr.ib(type=List[ProtectedRangeUpdate], default=None, metadata={'json': 'requests'})


@attr.s
class SpreadsheetsProtectedRangeBatchUpdateResult(object):
    replies = attr.ib(type=List[ProtectedRangeUpdate], default=None, metadata={'json': 'replies'})


@to_json_decorator
@attr.s
class SpreadsheetsSheetsBatchUpdateReqBody(object):
    requests = attr.ib(type=List[Request], default=None, metadata={'json': 'requests'})


@attr.s
class SpreadsheetsSheetsBatchUpdateResult(object):
    replies = attr.ib(type=List[Reply], default=None, metadata={'json': 'replies'})


@to_json_decorator
@attr.s
class SpreadsheetsSheetsUpdatePropertiesReqBody(object):
    properties = attr.ib(type=Properties, default=None, metadata={'json': 'properties'})


@attr.s
class SpreadsheetsSheetsUpdatePropertiesResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    title = attr.ib(type=str, default=None, metadata={'json': 'title'})


@to_json_decorator
@attr.s
class SpreadsheetsStyleUpdateReqBody(object):
    append_style = attr.ib(type=AppendStyle, default=None, metadata={'json': 'appendStyle'})


@attr.s
class SpreadsheetsStyleUpdateResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    updated_range = attr.ib(type=str, default=None, metadata={'json': 'updatedRange'})
    updated_rows = attr.ib(type=int, default=None, metadata={'json': 'updatedRows'})
    updated_columns = attr.ib(type=int, default=None, metadata={'json': 'updatedColumns'})
    updated_cells = attr.ib(type=int, default=None, metadata={'json': 'updatedCells'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})


@to_json_decorator
@attr.s
class SpreadsheetsStylesBatchUpdateReqBody(object):
    data = attr.ib(type=AppendStyleBatch, default=None, metadata={'json': 'data'})


@attr.s
class SpreadsheetsStylesBatchUpdateResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    total_updated_rows = attr.ib(type=int, default=None, metadata={'json': 'totalUpdatedRows'})
    total_updated_columns = attr.ib(type=int, default=None, metadata={'json': 'totalUpdatedColumns'})
    total_updated_cells = attr.ib(type=int, default=None, metadata={'json': 'totalUpdatedCells'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})
    responses = attr.ib(type=List[UpdateResponse], default=None, metadata={'json': 'responses'})


@to_json_decorator
@attr.s
class SpreadsheetsUnmergeCellsReqBody(object):
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})


@attr.s
class SpreadsheetsUnmergeCellsResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})


@to_json_decorator
@attr.s
class SpreadsheetsValuesAppendReqBody(object):
    value_range = attr.ib(type=ValueRange, default=None, metadata={'json': 'valueRange'})


@attr.s
class SpreadsheetsValuesAppendResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    table_range = attr.ib(type=str, default=None, metadata={'json': 'tableRange'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})
    updates = attr.ib(type=Updates, default=None, metadata={'json': 'updates'})



@attr.s
class SpreadsheetsValuesBatchGetResult(object):
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    total_cells = attr.ib(type=int, default=None, metadata={'json': 'totalCells'})
    value_ranges = attr.ib(type=List[ValueRange], default=None, metadata={'json': 'valueRanges'})


@to_json_decorator
@attr.s
class SpreadsheetsValuesBatchUpdateReqBody(object):
    value_ranges = attr.ib(type=List[ValueRange], default=None, metadata={'json': 'valueRanges'})


@attr.s
class SpreadsheetsValuesBatchUpdateResult(object):
    responses = attr.ib(type=List[UpdateResponse], default=None, metadata={'json': 'responses'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})



@attr.s
class SpreadsheetsValuesGetResult(object):
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    value_range = attr.ib(type=ValueRange, default=None, metadata={'json': 'valueRange'})


@to_json_decorator
@attr.s
class SpreadsheetsValuesImageReqBody(object):
    range = attr.ib(type=str, default=None, metadata={'json': 'range'})
    image = attr.ib(type=List[int], default=None, metadata={'json': 'image'})
    name = attr.ib(type=str, default=None, metadata={'json': 'name'})


@attr.s
class SpreadsheetsValuesImageResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})


@to_json_decorator
@attr.s
class SpreadsheetsValuesPrependReqBody(object):
    value_range = attr.ib(type=ValueRange, default=None, metadata={'json': 'valueRange'})


@attr.s
class SpreadsheetsValuesPrependResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    table_range = attr.ib(type=str, default=None, metadata={'json': 'tableRange'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})
    updates = attr.ib(type=Updates, default=None, metadata={'json': 'updates'})


@to_json_decorator
@attr.s
class SpreadsheetsValuesUpdateReqBody(object):
    value_range = attr.ib(type=ValueRange, default=None, metadata={'json': 'valueRange'})


@attr.s
class SpreadsheetsValuesUpdateResult(object):
    spreadsheet_token = attr.ib(type=str, default=None, metadata={'json': 'spreadsheetToken'})
    updated_range = attr.ib(type=str, default=None, metadata={'json': 'updatedRange'})
    updated_rows = attr.ib(type=int, default=None, metadata={'json': 'updatedRows'})
    updated_columns = attr.ib(type=int, default=None, metadata={'json': 'updatedColumns'})
    updated_cells = attr.ib(type=int, default=None, metadata={'json': 'updatedCells'})
    revision = attr.ib(type=int, default=None, metadata={'json': 'revision'})