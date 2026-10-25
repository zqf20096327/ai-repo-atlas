# tjx666/vscode-classic-experience

⭐ 56 · TypeScript · MIT · 推送 2025-11-02 · [GitHub](https://github.com/tjx666/vscode-classic-experience) · [官网](https://marketplace.visualstudio.com/items?itemName=YuTengjing.vscode-classic-experience) · 个人维护

**在 Cursor 编辑器中恢复 VSCode 原生快捷键的扩展**

面向从 VSCode 迁移到 Cursor 的用户的编辑器扩展：通过扩展 API 移除部分 Cursor 快捷键并恢复 VSCode 原有快捷键（如 ⌘K 前缀、⌘L 行选择、⇧⌘K 删除行等），不修改 Cursor 设置或本地文件，禁用或卸载即可还原。附带 .cursor/mcp.json 的 JSON schema 校验说明与恢复 VSCode 活动栏布局的配置示例。主要在 macOS 上开发测试，Windows/Linux 兼容性未经充分验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 移除 ⌘R 前缀快捷键并恢复 VSCode 的 ⌘K 前缀体系
- 调整 ⌘L / ⇧⌘L / ⇧⌘K 等被 Cursor 修改的常用快捷键
- 提供 .cursor/mcp.json 的 JSON validate schema
- 卸载或禁用即可还原，不修改 Cursor 设置或本地文件

## 适用场景

- 从 VSCode 切换到 Cursor 后沿用熟悉的键盘快捷键
- 恢复 VSCode 风格的活动栏与侧边栏布局
- 为 .cursor/mcp.json 配置文件获得 schema 校验

## 场景标签

 · 领域:开发工具/编辑器扩展

## 证据(README 行号)

> L13: Seamlessly restore the familiar VSCode keybindings in Cursor with a single installation. This extension brings back
> L67: ## Windows and Linux

## 星数曲线

```mermaid
xychart-beta
    title "tjx666/vscode-classic-experience 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-25 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `4bd7ea6e0c16` · [字段定义](../../DATASET.md)*
