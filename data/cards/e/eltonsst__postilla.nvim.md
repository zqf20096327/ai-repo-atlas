# eltonsst/postilla.nvim

⭐ 21 · Lua · MIT · 推送 2026-08-20 · [GitHub](https://github.com/eltonsst/postilla.nvim) · 个人维护

**Neovim 插件：逐行给 AI 代理代码写行内评审注释并导出反馈**

面向 AI-agent 编码工作流的 Neovim 插件：在不修改源文件的前提下给指定行或行区间附加多行注释，在底部分屏编写评论且被审代码保持可见。审阅完成后将全部注释以 revdiff 标注格式复制到剪贴板，可直接粘贴给 Codex 等编码代理。支持注释随代码移动重定位、被审代码变更时警告并阻断导出、会话跨 Neovim 重启恢复。要求 Neovim 0.10+，Git 与剪贴板支持为推荐项。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对精确行/行区间附加多行注释且不改动源文件
- 代码移动时保持注释附着，代码变更时警告并阻断导出
- revdiff 标注格式导出到剪贴板，注释关联文件与行号
- 评审会话存储在项目外，重启后可恢复

## 适用场景

- 在 Neovim 中逐行审查 AI 代理写的代码
- 把结构化的行级反馈粘贴回 Codex 等编码代理继续对话
- 中途暂停评审并跨会话恢复未完成的注释

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L7: **Review the code your agent wrote, line by line, inside Neovim.**
> L10: When the review is done, it copies structured feedback to your clipboard, ready
> L11: to paste into Codex or another coding agent.

## 星数曲线

```mermaid
xychart-beta
    title "eltonsst/postilla.nvim 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `6e40c4fc8f12` · [字段定义](../../DATASET.md)*
