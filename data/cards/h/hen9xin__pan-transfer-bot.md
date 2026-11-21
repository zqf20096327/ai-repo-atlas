# hen9xin/pan-transfer-bot

⭐ 4 · Python · MIT · 推送 2026-10-15 · [GitHub](https://github.com/hen9xin/pan-transfer-bot) · 个人维护 · 中文 README

**为 Claude Code 提供 Quark/Baidu Pan 资源传输及文案撰写功能的 Agent skill**

面向个人网盘资源整理工作流的工具：输入包含网盘链接的文本后，识别网盘类型、穿透短链、提取提取码，将文件转存至用户自己账号并按年/月/日归档，再生成新的分享链接与配套文案。文案由本地确定性引擎生成，不依赖外部大模型 API；可通过 Web 界面、REST API 使用，也可作为 SKILL.md 被 Claude Code 等 AI Agent 调用。使用需自行配置网盘 Cookie，服务自身不带登录鉴权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 自动识别夸克/百度网盘链接并穿透短链、提取提取码
- 转存到个人网盘并按年/月/日归档，生成用户账号下的分享链接
- 内置本地确定性文案引擎，离线可用、无 API 费用
- 提供 SKILL.md，可安装到 Claude Code 等支持 SKILL.md 的 Agent

## 适用场景

- 把自己收藏的网盘分享链接批量转存并按日期归档
- 转发资源时生成配文与个人分享链接
- 通过 Claude Code 对话方式调用转存与文案接口

## 场景标签

 · 领域:个人效率/网盘自动化

## 证据(README 行号)

> L3: **给 AI Agent 用的夸克 / 百度网盘资源整理 Skill + 本地文案助手**
> L27: 4. **本地生成配套文案**：内置纯本地改写与排版算法（句式调整、Emoji、标签），无需任何外部大模型 API Key。
> L29: 可以通过 **Web 界面**、**REST API**，或作为 **Agent Skill**（SKILL.md）让 Claude Code 等 AI Agent 直接调用。
> L42: |⚡ **零外部 AI 依赖**|内置本地确定性文案引擎（`services/text_generator.py`），离线可用、无 API 费用。|

## 星数曲线

```mermaid
xychart-beta
    title "hen9xin/pan-transfer-bot 星数(近 3 点)"
    x-axis ["2026-10-19", "2026-10-22", "2026-11-21"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-10-19 3 → 2026-11-21 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `e7d187872049` · [字段定义](../../DATASET.md)*
