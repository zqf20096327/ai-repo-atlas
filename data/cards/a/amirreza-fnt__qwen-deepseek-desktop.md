# amirreza-fnt/qwen-deepseek-desktop

⭐ 3 · Python · NOASSERTION · 推送 2026-11-21 · [GitHub](https://github.com/amirreza-fnt/qwen-deepseek-desktop) · 个人维护

**Windows 桌面端 Qwen/DeepSeek 编码助手客户端，带 diff 审查**

基于 PySide6/Qt 6 的 Windows 桌面应用，将 Qwen 与 DeepSeek 网页版聊天整合进一个原生窗口，需用户使用自己的账号 web 会话登录。提供聊天内逐行流式代码输出、Project mode（模型提出整文件/SEARCH-REPLACE 编辑，用户以 diff 审查后应用，带备份与撤销）、以及需点击批准才执行的 agent 工具（读/搜文件自动执行，命令/下载/外部请求需批准）。界面支持英语与波斯语（RTL）。依赖私有网页接口，可能随服务方变更而失效。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 一个应用内接入 Qwen 与 DeepSeek 网页聊天，内置浏览器完成登录
- Project mode：模型提出文件改动，用户以统一/并排 diff 审查后应用，支持撤销
- Agent 工具分级执行：只读操作自动运行，命令/下载/外部请求需点击批准
- 令牌存于 Windows Credential Manager，聊天历史保存在本地 SQLite

## 适用场景

- 在桌面窗口里同时使用 Qwen 和 DeepSeek 讨论代码
- 让模型提出项目文件改动，逐个 diff 审查后再应用
- 在受控批准机制下让模型执行命令与检索文件

## 场景标签

`编码 Agent` `代码审查` `AI 助手` `代码生成` · 领域:编码与开发

## 证据(README 行号)

> L3: **A free, open-source desktop AI coding assistant for Windows — chat with Qwen and DeepSeek in one app, stream full 
> L19: The web chats of Qwen and DeepSeek are great at code, but copying code back and forth into your editor is slow. Thi

## 星数曲线

```mermaid
xychart-beta
    title "amirreza-fnt/qwen-deepseek-desktop 星数(近 2 点)"
    x-axis ["2026-11-25", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-25 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `4389de9d68cf` · [字段定义](../../DATASET.md)*
