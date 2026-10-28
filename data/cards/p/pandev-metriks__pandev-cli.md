# pandev-metriks/pandev-cli

⭐ 25 · Shell · NOASSERTION · 推送 2026-10-20 · [GitHub](https://github.com/pandev-metriks/pandev-cli) · [官网](https://pandev-metrics.com/cli) · 组织维护

**本地分析 AI 编程代理开销的 CLI：按任务/分支/模型/文件拆分成本**

读取本机的 Claude Code、Codex CLI、opencode、ZCode 日志，把 token 花费按任务、分支、模型、文件与单条 prompt 归因统计，通过 git reflog 重建真实分支以修正日志中 HEAD 导致的归因偏差。提供终端命令与仅监听 127.0.0.1:4976 的本地仪表盘、可登录自启、离线单文件副本。无遥测、无账号；闭源专有许可，Node 20+，git 可选（缺失则关闭任务归因）。面向个人开发者，团队场景指向另一产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从本地日志按任务/分支/模型/文件/单条 prompt 归因成本
- 用 git reflog 重建时间戳对应的真实分支
- 本地回环仪表盘与零网络请求的离线 HTML 副本
- 声明二进制无出站网络调用，并提供外部验证文档

## 适用场景

- 查看我每个工单/任务花了多少 AI 费用
- 分析缓存读写在 token 用量中的占比
- 订阅制下核算按 API 费率折算的实际开销

## 场景标签

`LLM 可观测性` · 领域:评测与运维

## 证据(README 行号)

> L36: Your agent bills you per token. Your work is organised in tasks. Nothing connects the two.
> L174: Reads logs from:

## 星数曲线

```mermaid
xychart-beta
    title "pandev-metriks/pandev-cli 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `dfe83fc655a0` · [字段定义](../../DATASET.md)*
