# mythril-tech-com/Claude_Code_Helper

⭐ 3 · TypeScript · MIT · 推送 2026-11-02 · [GitHub](https://github.com/mythril-tech-com/Claude_Code_Helper) · [官网](https://marketplace.visualstudio.com/items?itemName=mythriltech.claude-code-add-to-chat) · 个人维护

**VS Code 扩展：右键把文件/行引用加入 Claude Code 聊天**

VS Code 扩展，为 Claude Code 提供类似 Cursor 的 'Add to chat' 操作：通过右键菜单、`Ctrl+L` 快捷键或拖放，将文件、文件夹或选中行的 @引用 加入 Claude Code 聊天。依赖 Claude Code 扩展，也可通过 Open VSX 安装到 Cursor、Windsurf 等基于 VS Code 的编辑器。扩展本身不发送网络请求、不收集遥测、不读取文件内容，引用经剪贴板 basket 机制注入聊天。设置项覆盖自动粘贴、basket 自动清理与 Tab 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 右键文件/文件夹/选中行生成 @引用，支持多选
- `Ctrl+L`/`Cmd+L` 将选中行加入 Claude 聊天
- 拖放条带恢复 VS Code 1.140 后失效的拖放路径
- 无网络请求、无遥测、不读取文件内容

## 适用场景

- 在 VS Code 中引用多个文件向 Claude Code 提问
- 选中具体代码行让 Claude 定位讨论范围
- 在 Cursor/Windsurf 等编辑器中添加文件引用到 Claude 聊天

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Add file, folder and line references to the Claude Code chat, similar to Cursor's "Add to chat". Right-click files i
> L5: Requires the Claude Code extension (VS Code Marketplace, Open VSX). In Cursor, Antigravity, Windsurf and other edito

## 星数曲线

```mermaid
xychart-beta
    title "mythril-tech-com/Claude_Code_Helper 星数(近 2 点)"
    x-axis ["2026-11-01", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-01 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `ec7c868270a6` · [字段定义](../../DATASET.md)*
