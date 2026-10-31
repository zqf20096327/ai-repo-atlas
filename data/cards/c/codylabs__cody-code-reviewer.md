# codylabs/cody-code-reviewer

⭐ 13 · Python · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/codylabs/cody-code-reviewer) · [官网](https://docs.codylabs.uk/) · 组织维护

**GitHub Actions 内私有 AI 代码审查：BYOK 审查 PR 并评论**

以 GitHub Action 形式运行的拉取请求审查工具：在用户自己的 runner 内将 diff 直接发送到所选的 OpenAI 或 Anthropic 模型，以单条评论形式发布发现的问题，后续 push 更新同一评论而非追加。BYOK 模式，仅支付模型提供商使用费。支持从 base commit 读取 AGENTS.md/REVIEW.md/CLAUDE.md 等指令文件，可设置 max_review_rounds 上限、exclude_paths 排除路径、max_diff_chars 截断。仅覆盖 GitHub PR；GitLab/Azure DevOps 由付费版 Cody Pro 提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Action 在用户自己的 GitHub runner 内运行，diff 直接发送模型提供商，Cody Labs 不接收代码
- 从 base commit 读取 AGENTS.md/REVIEW.md/CLAUDE.md 等可信指令文件
- max_review_rounds 审查轮次上限与 cody:force-review 标签强制审查
- 后续 push 更新既有评论，并按 max_diff_chars 截断发送 diff

## 适用场景

- 私有仓库在不引入第三方审查服务的前提下做 AI PR 审查
- 让 AI 按仓库自定义规则文件审查代码变更
- 控制长 PR 往返中的审查成本与轮次

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: Cody reviews GitHub pull requests with an OpenAI or Anthropic model of your choice, then
> L8: Cody runs inside your own GitHub Actions job and sends the diff directly to the model
> L9: provider using your API key. The inspected, unmodified Action contains no Cody Labs

## 星数曲线

```mermaid
xychart-beta
    title "codylabs/cody-code-reviewer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 12 --> 14
    line [13, 13]
```

2026-10-18 13 → 2026-10-31 13（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `00e5e68dacc7` · [字段定义](../../DATASET.md)*
