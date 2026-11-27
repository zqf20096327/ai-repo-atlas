# aqiu817/magpie-amd-cloud

⭐ 4 · JavaScript · MIT · 推送 2026-11-13 · [GitHub](https://github.com/aqiu817/magpie-amd-cloud) · 个人维护 · 中文 README

**把 AMD 两个免费模型 API 站点接入 magpie 的零依赖供应商插件**

OpenCode v1 形式的 magpie 供应商插件，接入 AMD Radeon Cloud（developer.amd.com.cn）与 TokenLab（api.tokenlab.amd.com）两个免费共享模型 API，以文件夹就地加载，零依赖零构建。功能包括：运行时从各自 /v1/models 拉取聊天模型目录（国内站 10 个聊天模型）、多 key 多账号登录、国内站 24h 滚动点数窗口展示与 magpie quota 输出、国际站本地预估用量、推理档位映射（reasoning_effort→variants）、401 重登标记与 429/5xx 故障切换（magpie 原生行为）。模型过滤仅保留聊天模态；通过 `magpie plugin add` 加载。

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

- 双站点供应商：国内站 amd-cloud 与国际站 amd-cloud-lab，可同时登录
- 运行时拉取模型目录，新模型上架自动出现，非聊天条目自动过滤
- 额度展示：国内站 24h 滚动点数窗口、国际站本地预估用量，经 GET /v1/magpie/quotas 暴露给外部工具
- 支持 DeepSeek-V4-Flash 六档与 Qwen3.8-Flash-Next 四档推理档位映射

## 适用场景

- 让 Claude Code、Codex、OpenCode 等 Agent 通过 magpie 调用 AMD 免费 API 上的模型
- 在 magpie 中集中查看 AMD 云多账号的额度与用量
- 为接入期内的 AMD AI Developer Program 账号做 key 登录与故障切换管理

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5: 把 AMD 的**两个免费共享模型 API 站点**接入 magpie，变成供应商插件：
> L12: 接入后 Claude Code、Codex、OpenCode 等所有 Agent 都能通过 magpie 调用 Radeon GPU 上的模型，额度直接显示在 magpie 里。插件本身零依赖、零构建：一个 OpenCode v1
> L35:    magpie plugin add /path/to/magpie-amd-cloud   # 文件夹就地加载

## 星数曲线

```mermaid
xychart-beta
    title "aqiu817/magpie-amd-cloud 星数(近 3 点)"
    x-axis ["2026-11-10", "2026-11-11", "2026-11-27"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-10 3 → 2026-11-27 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `c460465eea70` · [字段定义](../../DATASET.md)*
