# flyteorg/flyteconsole

⭐ 45 · TypeScript · Apache-2.0 · 推送 2026-10-25 · [GitHub](https://github.com/flyteorg/flyteconsole) · [官网](https://github.com/flyteorg/flyte) · 组织维护

**Flyte 机器学习工作流平台的 Web 管理界面**

Flyte 平台的 Web 前端控制台：从 FlyteAdmin API 读取数据，展示工作流与执行信息，支持动态执行与长时间运行工作流的时间线视图。面向使用 Flyte 做机器学习/MLOps 编排的开发者与团队。本地运行需 NodeJS 与 yarn，可配合 docker 沙箱后端启动，也提供 docker 镜像直接运行；通过 ADMIN_API_URL、BASE_URL 等环境变量配置 API 地址与部署前缀。开发层面提供 Storybook 组件测试、Protobuf Debug 输出与特性开关。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 读取 FlyteAdmin API 展示工作流与执行信息
- 支持动态执行与长时间运行工作流的时间线
- 提供 docker 镜像与 yarn 本地开发两种运行方式
- Storybook 组件测试与特性开关机制

## 适用场景

- 在浏览器中查看和监控 Flyte 工作流执行状态
- 配合 Flyte 沙箱后端搭建本地开发调试环境
- 部署在集群中作为团队的 MLOps 管理入口

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L7:  Web UI for the Flyte platform
> L89:  The Flyte Console displays information fetched from the FlyteAdmin API. This

## 星数曲线

```mermaid
xychart-beta
    title "flyteorg/flyteconsole 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-26 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `6a71b65f32db` · [字段定义](../../DATASET.md)*
