# htlin222/oe-extension

⭐ 14 · JavaScript · MIT · 推送 2026-09-09 · [GitHub](https://github.com/htlin222/oe-extension) · 个人维护

**把选中文字直接送入 OpenEvidence 的 Chrome 扩展，含 PICO 改写**

面向临床医生、学生与循证医学读者的 Chrome 扩展：在白名单页面选中文本后，一键在当前标签旁打开 OpenEvidence 查询，并提供 UpToDate/Google 旁路搜索、右键菜单、本地查询历史、白名单激活与 NCCN 指南链接重定向。AI 部分：用户自带 Groq API key（存于 chrome.storage.local）后可将回忆式选文改写为可编辑的前景 PICO 问题，或运行自定义提示词按钮，LLM 输出在可编辑面板中展示。无运行时框架依赖，从 Release zip 或源码构建安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选中文字一键在旁侧标签打开 OpenEvidence 查询
- BYOK Groq 集成：PICO 改写与自定义提示词按钮，输出可编辑后送查
- 本地查询历史与白名单激活（含 file:///*）
- NCCN 指南 PDF 链接重定向到用户自定查看器

## 适用场景

- 在 UpToDate/NEJM 等页面阅读时把疑问直接送入 OpenEvidence
- 把病例回忆式文本改写为结构化 PICO 前景问题再检索
- 绕过 NCCN 登录墙，用本地 PDF 查看指南引用

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L10: OpenEvidence Selection Opener is a lightweight Chrome extension for clinicians,
> L13: right next to the current tab. With a validated Groq API key, it can also rewrite

## 星数曲线

```mermaid
xychart-beta
    title "htlin222/oe-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `b301fb31c2da` · [字段定义](../../DATASET.md)*
