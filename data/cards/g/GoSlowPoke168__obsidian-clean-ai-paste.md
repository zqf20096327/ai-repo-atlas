# GoSlowPoke168/obsidian-clean-ai-paste

⭐ 14 · JavaScript · MIT · 推送 2026-10-23 · [GitHub](https://github.com/GoSlowPoke168/obsidian-clean-ai-paste) · 个人维护

**Obsidian 插件：自动清理粘贴自 AI 聊天界面的杂乱文本**

Obsidian 社区插件，拦截外部粘贴事件，将剪贴板 HTML 转换为原生 Markdown，并应用可配置的格式化规则：空行规范化、去除表情与链接跟踪参数、去粗体标题、LaTeX 分隔符转换、代码块智能处理（语言标签绑定、单行转行内代码）等。支持 Ctrl+Shift+V 绕过格式化、调试预览三面板、跟踪签名标记 AI 内容。兼容 Obsidian 0.15.0+ 桌面与移动端，可从社区插件商店安装。已知限制：部分 AI 界面复制的代码丢失 HTML 结构时无法识别为代码块。

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

- 拦截外部粘贴并执行 HTML→Markdown 转换与可配置格式化规则
- 代码块智能处理：语言标签绑定、单行块转行内代码、重复标签去除
- 去除表情（含白名单）与 URL 跟踪参数（utm_source 等）
- Ctrl+Shift+V 绕过格式化与三面板调试预览模式

## 适用场景

- 把 ChatGPT/Claude 等对话内容整理成干净的 Markdown 笔记
- 去除 AI 输出中的多余空行、表情和链接跟踪参数
- 粘贴时保留 ASCII 表格与对齐内容的原始格式

## 场景标签

 · 领域:笔记/文本处理工具

## 证据(README 行号)

> L7: **Clean AI Paste** is an Obsidian plugin designed to automatically clean up and format text pasted from AI chatbots 
> L9: When you copy text from an AI web interface, the result in Obsidian is often cluttered with excessive blank lines, m
> L86: 3. **HTML → Markdown conversion** — Reads `text/html` from the clipboard and converts it to native Markdown using O

## 星数曲线

```mermaid
xychart-beta
    title "GoSlowPoke168/obsidian-clean-ai-paste 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 12 --> 15
    line [13, 14, 14]
```

2026-10-18 13 → 2026-10-31 14（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `035a4af25f45` · [字段定义](../../DATASET.md)*
