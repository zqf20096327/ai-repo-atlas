# open-world-project/model-router

⭐ 32 · Python · MIT · 推送 2026-05-10 · [GitHub](https://github.com/open-world-project/model-router) · 组织维护

**Hermes Agent 的成本感知模型路由插件：按轮次分档选模型**

Hermes Agent 的 Python 插件，在每轮对话前由分类器判定任务难度，在固定的五个模型层级（T1-T5）中选取成本最低的可用档位；工具调用连续失败 2 次自动升档（最高自动升至 T4），轮次完成后自动降回基础档。支持 /t1-/t5 与 /auto 手动固定、按 profile 的 model_router.yaml 配置、安装器自动校验并修复 Hermes 核心补丁文件（含备份），并可给 hermes-webui 打补丁以在 WebUI 中暴露原生层级控制。默认围绕 OpenRouter 配置与测试，非 OpenRouter 供应商依赖 Hermes 的 triage_specifier 支持。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 每轮分类后从五档（T1-T5）中选最低成本模型
- 工具连续失败 2 次自动升档，轮次结束自动降档
- install.sh 校验并修复 Hermes 核心补丁，重复运行安全
- 与 hermes-webui 集成：WebUI 原生 Auto/T1-T5 控制

## 适用场景

- Hermes Agent 用户降低日常对话的模型调用成本
- 简单任务走低档、复杂规划自动用高档模型
- 多 profile（seo/coder/trading）分别配置路由档位

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L3: Automatic cost-aware model routing for Hermes Agent.
> L9: - automatic per-turn routing,

## 星数曲线

```mermaid
xychart-beta
    title "open-world-project/model-router 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-27 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `336eb9a50034` · [字段定义](../../DATASET.md)*
