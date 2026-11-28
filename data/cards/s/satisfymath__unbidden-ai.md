# satisfymath/unbidden-ai

⭐ 5 · Python · Apache-2.0 · 推送 2026-11-15 · [GitHub](https://github.com/satisfymath/unbidden-ai) · [官网](https://unbidden.cl) · 个人维护

**主动式工程 Agent CLI：在沙箱验证改进并以 PR 附证据提出**

以 CLI 形式安装到仓库中的主动式工程 Agent：在离线沙箱中运行团队自有检查，寻找可证明的改进、测量效果，并生成携带证据的 pull request；按授权等级可执行合并、部署、监控与回滚，设有证据分级（L1–L6）、自主模式（supervised/autopilot/autonomous）、egress 审计与隐私桥（出站前重命名私有代码）。模型经 Ollama 本地运行或 Meta API 调用，敏感数据仅限本地模型处理。为实验性候选版本，支持 macOS Apple Silicon 与 Linux x86-64。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 证据分级 L1–L6，默认仅 L4 及以上才生成 pull request
- 三档数据路由（local/mixed/api），密钥与生产数据不出机器
- supervised/autopilot/autonomous 三种自主模式，unbidden kill 可全进程冻结
- unbidden export 输出脱敏记录、模型调用转录与 sha256 清单

## 适用场景

- 让 Agent 在沙箱中验证性能改进后自动提交 PR
- 自动发现并修复代码中的缺陷并附测试证据
- 部署异常时自动回滚并锁定等待人工放行

## 场景标签

`编码 Agent` `代码审查` · 领域:编码与开发

## 证据(README 行号)

> L18: Unbidden is a proactive engineering agent you install like a CLI. It lives in a repository, runs the team's
> L23: It runs on Meta models. **Muse Glimmer** runs locally through Ollama and is the only model that ever sees

## 星数曲线

```mermaid
xychart-beta
    title "satisfymath/unbidden-ai 星数(近 3 点)"
    x-axis ["2026-11-08", "2026-11-15", "2026-11-28"]
    y-axis "stars" 3 --> 6
    line [4, 5, 5]
```

2026-11-08 4 → 2026-11-28 5（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `85c16f722944` · [字段定义](../../DATASET.md)*
