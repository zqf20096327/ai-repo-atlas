# mofe-stack/continuum

⭐ 15 · JavaScript · MIT · 推送 2026-08-10 · [GitHub](https://github.com/mofe-stack/continuum) · [官网](https://continuum-capture.netlify.app) · 组织维护 · 中文 README

**浏览器扩展：保存/导出 AI 聊天并跨站点恢复上下文**

面向使用 Claude、ChatGPT、Gemini、Perplexity 的浏览器扩展：一键抓取完整对话（含可及的图片/文件），在新聊天中回灌历史实现跨站点续聊，并可导出 Markdown 或 PDF。本地优先：无账号、无后端、无遥测，数据仅存于本设备。提供可选的 AI 压缩（用户自己的 API key，把长对话压成七节结构简报，默认关闭）。附件捕获能力受各站点 DOM 限制（部分仅记文件名）。通过 Chrome/Firefox 商店分发，也可用 Node 脚本本地构建加载。

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

- 跨站点捕获与恢复：一处抓取的聊天可续到另一家 AI 站点
- 本地优先：无账号、无服务器、无追踪
- 导出 Markdown / PDF，界面支持 11 种语言
- 可选 AI 压缩：用自有 API key 将长对话压成七节结构简报（默认关闭）

## 适用场景

- 对话达到长度上限时，把完整上下文带到新聊天继续
- 把不同 AI 站点的对话迁移到另一家续问
- 把 AI 聊天导出为 Markdown 或 PDF 存档

## 场景标签

 · 领域:AI 对话工具/浏览器扩展

## 证据(README 行号)

> L5: Continuum is a browser extension that captures an AI chat session and lets you pick it back up in a fresh chat, so y
> L19: - **Capture a chat.** Click the Continuum button on a supported AI site and it grabs the whole conversation — messa
> L20: - **Resume somewhere else.** Open a new chat on a supported site and Continuum drops the captured history back in, 
> L21: - **Save and export.** Captured sessions are kept locally and can be exported to Markdown or PDF.

## 星数曲线

```mermaid
xychart-beta
    title "mofe-stack/continuum 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e913bf2f5356` · [字段定义](../../DATASET.md)*
