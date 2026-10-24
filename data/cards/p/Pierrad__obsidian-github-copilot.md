# Pierrad/obsidian-github-copilot

⭐ 499 · TypeScript · Apache-2.0 · 推送 2026-05-03 · [GitHub](https://github.com/Pierrad/obsidian-github-copilot) · 个人维护

**在 Obsidian 编辑器中接入 GitHub Copilot 的插件（补全+聊天）**

连接 Obsidian 笔记编辑器与 GitHub Copilot 服务的社区插件，面向持有 Copilot 订阅的 Obsidian 用户。提供两类功能：输入时的行内代码/文本补全（可配置延迟、按键绑定、仅代码块或全文、排除文件目录），以及右侧栏 Copilot Chat（可选 gpt-4、claude 3.7 等服务可用模型，支持聊天历史、双链笔记引用、系统提示词配置与 Mermaid 图渲染，流式输出尚未实现）。行内补全需本机 Node.js 22+ 二进制；通过 Obsidian 社区插件浏览器安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GitHub Copilot 行内补全：可配置延迟、按键绑定与作用范围
- Copilot Chat：可选服务可用模型，支持聊天历史与双链笔记引用
- 聊天回复中渲染 Mermaid 图表
- 需 GitHub Copilot 订阅与本机 Node.js 22+ 二进制

## 适用场景

- 在 Obsidian 笔记中编写时获得 Copilot 行内补全
- 用 Copilot Chat 问答、总结或链接自己的笔记
- 让 Copilot 生成并在聊天中渲染流程图等 Mermaid 图表

## 场景标签

`代码生成` `聊天机器人` · 领域:编码与开发

## 证据(README 行号)

> L6: Use **GitHub Copilot** in the Obsidian editor. This plugin is a bridge between the Obsidian editor and the GitHub Co
> L8: - 🤖 Get inline suggestion as you type using GitHub Copilot service
> L9: - 💬 Use the GitHub Copilot Chat service to ask questions about your notes

## 星数曲线

```mermaid
xychart-beta
    title "Pierrad/obsidian-github-copilot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 497 --> 500
    line [498, 499]
```

2026-10-18 498 → 2026-10-24 499（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `236ef18d3bca` · [字段定义](../../DATASET.md)*
