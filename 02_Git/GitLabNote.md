GitLabNote
===

要望

- ユーザフォロー機能入れろ。マジで。
- 好きなプロジェクトをユーザトップに表示させろ。マジで。


## GitHub 開発フロー

1. Milestone 作成
    - 例: `v.1.0.0 Initial release`
1. Issue 作成
    - 追加機能やバグはすべて Issue で管理。
    - Milestone と Assignees を設定する。Assignees が実装を行う。
1. Branch と PR を作成。
    - Issue ページから一気に行える! GitHub に大幅に差をつけているところだ。
    - ブランチ名は `ユーザ名/機能名(_区切り)`
1. Commit, Push
    - ブランチを落としてきて開発。
    - 試行錯誤の過程は除くこと。
    - コミットメッセージは英語で。
    - バグ修正は `Fix + 修正内容 + (Issue番号)` `ex. Fix entry dialog (#1)`
    - 機能追加は `Add + 追加内容 + (Issue番号)` `ex. Add entry dialog (#1)`    
1. レビュー準備が出来たら
    - Reviewers, Assignees, Labels, Milestone 設定
    - `[WIP]` を外して Reviewers へ mention を送る。
    - PR のコメントに `fixes #ISSUE番号` をつけるとマージと同時に issue を閉じてくれる。


## Slackと連携

Slack側

1. https://slack.com/apps/A0F7XDUAZ--web-
1. Add Configuration

Gitlab側

1. 対象プロジェクト > Settings > Integrations > Slack notifications
1. Active にチェック入れる。
1. Webhookにさっきのコピーをペースト。


## Issue と MergeRequest のテンプレート

- `.gitlab/issue_templates/***.md`
- `.gitlab/merge_request_templates/***.md`
- `***` 部分が issue と merge request のところで選べるようになる。
