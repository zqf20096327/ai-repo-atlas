# raullenchai/rapid-mlx-dsh-provider

⭐ 70 · JavaScript · Apache-2.0 · 推送 2026-08-19 · [GitHub](https://github.com/raullenchai/rapid-mlx-dsh-provider) · [官网](https://github.com/raullenchai/Rapid-MLX) · 个人维护

**DeepSeek Harness 的 Rapid-MLX 原生 provider 插件**

npm 发布的 dsh 插件，为 DeepSeek Harness 注册原生 rapid-mlx provider：从 Rapid-MLX 服务器的 /v1/models 读取模型事实（上下文窗口、reasoning parser、MoE/hybrid、模态），替代手工维护 settings.yaml；压缩按服务器报告的 max_model_len×thresholdRatio 计时。另注册 5 个模型管理工具与 /rapid-mlx 命令，经 CLI 拉取/删除模型。需 Node ≥22.15 与运行中的 Rapid-MLX 服务器，面向 Apple Silicon 本地 LLM 用户；部分服务器字段仅读取未自动应用，图像输入以 UNSUPPORTED 拒绝。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 /v1/models 读取模型事实，免手工配置，切模型自动跟随
- 压缩按服务器 max_model_len（统一内存实际容量）计时，而非广告窗口
- 注册 5 个模型管理工具（serving/cached/pull/remove/health）与 /rapid-mlx 总览命令
- 对官方 adapter 协议义务逐项实现并配测试

## 适用场景

- 在 Mac 上让 dsh 直接使用 Rapid-MLX 本地服务而免手写模型配置
- 会话内查看/拉取/删除本地模型与缓存
- 按机器统一内存实际容量对长对话做压缩计时

## 场景标签

 · 领域:LLM 基础设施/插件

## 证据(README 行号)

> L3: A native Rapid-MLX provider for
> L21: DSH can already talk to a local Rapid-MLX server through its generic
> L32: Rapid-MLX's `/v1/models` already publishes all of that and more. This adapter

## 星数曲线

```mermaid
xychart-beta
    title "raullenchai/rapid-mlx-dsh-provider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 69 --> 71
    line [70, 70]
```

2026-10-18 70 → 2026-10-30 70（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `799bc4d3d278` · [字段定义](../../DATASET.md)*
