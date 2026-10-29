# leopu00/job-hunter-team

⭐ 52 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/leopu00/job-hunter-team) · [官网](https://jobhunterteam.ai) · 个人维护

**自托管的 AI agent 团队，自动执行求职全流程**

多 agent 求职自动化系统：Captain 编排常驻角色（Sentinel 预算看护、Assistant、Mentor）与可伸缩的工作池（Scout 找职位、Analyst 验证、Scorer 按用户画像 0-100 打分、Writer 生成定制 CV 与求职信、Critic 三轮盲审）。各 agent 是运行在支持 CLI（Claude Code、Codex、Kimi）上的自主 AI 会话，SQLite 同步状态，整体运行在本地容器中。软件免费（MIT），但需约€40-200/月的专用 LLM 订阅；本地模型目前只能替代 Scorer。提供桌面安装包与 CLI 安装脚本两种安装方式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 多角色 agent 团队：发现、验证、打分、写作、盲审分工协作
- 容器化本地运行，共享 SQLite 同步状态，Captain 独立伸缩各角色
- 跨三平台提供桌面安装包（macOS 版已签名公证）与 CLI 安装脚本
- jht CLI 可由 Claude Code、OpenClaw、Codex、Cursor 等 AI 助手驱动

## 适用场景

- 让 agent 团队全天候扫描招聘板并筛选匹配职位
- 自动生成针对具体职位定制的 CV 与求职信
- 只人工复核通过质量门槛的申请材料

## 场景标签

`多智能体` · 领域:Agent 开发

## 证据(README 行号)

> L23: Job hunting is a second job on top of your job: scanning boards daily, qualifying listings, tailoring every applica
> L58: Each agent is an autonomous AI session on one of the supported CLIs (Claude Code, Codex, Kimi); a shared SQLite dat
> L25: Everything runs **locally in a container** — your machine or your VPS, your profile, your data, your provider accou

## 星数曲线

```mermaid
xychart-beta
    title "leopu00/job-hunter-team 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 50 --> 53
    line [51, 52, 52]
```

2026-10-18 51 → 2026-10-29 52（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `932ee964607b` · [字段定义](../../DATASET.md)*
