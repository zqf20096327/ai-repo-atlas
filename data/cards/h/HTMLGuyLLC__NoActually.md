# HTMLGuyLLC/NoActually

⭐ 7 · Rust · MIT · 推送 2026-11-19 · [GitHub](https://github.com/HTMLGuyLLC/NoActually) · 组织维护

**本地打分你与 AI 协作质量的桌面记分卡应用**

读取本机已有的 AI 工具聊天记录（Claude Code、Codex、ChatGPT 导出等），用固定规则本地计算 0-100 分，回答“AI 能否替代你”：统计提示一次说清的比例与双方谁在纠正谁，给出等级、周目标、连胜与奖章。评分不调用 AI、无需 API key、不上传数据，结果存于本地 SQLite。可选成绩单由用户自己的 AI 在 Claude Code/Codex 内生成，消耗其 token。仅支持英语评分。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯规则本地评分，同一历史始终同一分数，无需 API key
- 读取 Claude Code/Codex 实时记录及 ChatGPT/Claude.ai 数据导出
- 可选 /grade:me 成绩单由用户自己的 AI 生成（约 0.5k-2k token/次）
- 菜单栏/托盘常驻，MIT 开源，Mac 应用经 Apple 签名公证

## 适用场景

- 统计自己提示词一次说清的比例并设定改进目标
- 按模型、系列或具体版本分别查看纠错记录
- 生成可分享的成绩卡片发布到社交平台

## 场景标签

 · 领域:开发工具/AI 使用度量

## 证据(README 行号)

> L19: **No, Actually...** reads the chat history already on your computer and answers one big question, built from two sm
> L29: > **💸 Costs nothing to run.** No AI does the judging, so there's no API key, no tokens spent and no subscription. (
> L82: |🔒 **Local only**|No accounts, no servers, no telemetry, no analytics. Fonts are bundled. The app's only network us

## 星数曲线

```mermaid
xychart-beta
    title "HTMLGuyLLC/NoActually 星数(近 3 点)"
    x-axis ["2026-10-29", "2026-10-30", "2026-11-20"]
    y-axis "stars" 5 --> 8
    line [6, 7, 7]
```

2026-10-29 6 → 2026-11-20 7（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 mid · 依据 README sha `8b78605fe1a0` · [字段定义](../../DATASET.md)*
