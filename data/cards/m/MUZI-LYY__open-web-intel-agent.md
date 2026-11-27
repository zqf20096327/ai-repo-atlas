# MUZI-LYY/open-web-intel-agent

⭐ 10 · Python · MIT · 推送 2026-09-14 · [GitHub](https://github.com/MUZI-LYY/open-web-intel-agent) · 个人维护 · 中文 README

**给 AI Agent 提供本地化只读上网能力的工具集**

面向 AI Agent 的网页读取能力层：聚合六个渠道的抓取工具（urllib 网页转 Markdown、yt-dlp 读 YouTube 字幕/搜索/评论、gh CLI 读 GitHub、bili-cli 读 B站、V2EX 公开 API、feedparser 读 RSS），负责选型、安装与 doctor 环境体检，Agent 装好后直接调用上游工具。设计上只读公开内容、不经第三方中转、无需 API Key，明确不支持需登录的平台；安装默认只读检查，需显式 --system 才装系统依赖。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六个渠道装好即用：网页/YouTube/GitHub/B站/V2EX/RSS
- 本地抓取转 Markdown，数据不出本机，无需 API Key
- open-web-intel doctor 一条命令诊断各渠道连通状态
- 默认安全：install 默认只读，SSRF 防护拒绝内网地址

## 适用场景

- 让 Claude Code 等 Agent 自己安装并读取公开网页内容
- Agent 查询 YouTube 字幕、GitHub 仓库、B站视频信息
- 读取 RSS/Atom 源与 V2EX 公开讨论

## 场景标签

`网页抓取` · 领域:效率与自动化

## 证据(README 行号)

> L5:  给 AI Agent 装上网能力 —— 零登录、零 Cookie、零第三方数据服务，数据不出本机。
> L37: `Open-Web-Intel` 是**能力层（capability layer），不是包装层**。它负责三件事：
> L43: 装完之后，Agent **直接调用上游工具**（yt-dlp、gh、bili、feedparser），不经过中转。

## 星数曲线

```mermaid
xychart-beta
    title "MUZI-LYY/open-web-intel-agent 星数(近 2 点)"
    x-axis ["2026-10-25", "2026-11-27"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-25 10 → 2026-11-27 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `596b0554ba40` · [字段定义](../../DATASET.md)*
