# microsoft/vscode-copilot-vision

⭐ 78 · TypeScript · MIT · 推送 2026-10-21 · [GitHub](https://github.com/microsoft/vscode-copilot-vision) · 组织维护

**VS Code 扩展：让 GitHub Copilot 聊天支持图像输入与视觉问答**

Microsoft 维护的 VS Code 预览扩展（Copilot Vision Preview），在聊天面板中支持附加剪贴板/工作区图片或拖拽截图作为上下文输入，由用户自带 OpenAI、Azure OpenAI、Anthropic 或 Gemini API key 驱动，获得视觉支持的回答。另提供代码操作（Quick Fixes）为 Markdown、HTML、JSX、TSX 文档中的图片生成或精炼 alt 文本。README 声明该扩展即将被 VS Code 内置的 Copilot Chat 图像流取代（废弃）。

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

- 聊天面板附加图像作为上下文输入（剪贴板粘贴/拖拽/截图）
- 支持 OpenAI、Azure OpenAI、Anthropic、Gemini 等自带 API key 的视觉模型
- 为 Markdown/HTML/JSX/TSX 图片生成或精炼 alt 文本的 Quick Fix
- Troubleshoot 命令截取 VS Code 窗口发送到聊天，辅助屏幕阅读器用户诊断

## 适用场景

- 在 VS Code 聊天中以截图或设计图为上下文提问并获得代码回复
- 为文档与前端代码中的图片快速生成、修正 alt 文本
- 无障碍场景下通过截图诊断工作区问题

## 场景标签

`多模态` `AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L5: Vision for Copilot Preview is an extension that enhances chat interactions by enabling users to leverage advanced vi
> L8: For now, users can experience the image attachment flow in the chat panel by using their own OpenAI, Azure OpenAI, A
> L12: Additionally, users can generate or refine alt text for images in markdown, HTML, JSX, or TSX documents with the pr

## 星数曲线

```mermaid
xychart-beta
    title "microsoft/vscode-copilot-vision 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 77 --> 79
    line [78, 78]
```

2026-10-18 78 → 2026-10-28 78（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6b9755ee8231` · [字段定义](../../DATASET.md)*
