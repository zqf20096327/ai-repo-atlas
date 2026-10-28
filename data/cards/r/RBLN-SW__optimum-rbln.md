# RBLN-SW/optimum-rbln

⭐ 19 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/RBLN-SW/optimum-rbln) · [官网](https://docs.rbln.ai/software/optimum/optimum_rbln.html) · 组织维护

**把 HuggingFace 模型编译并运行在 RBLN NPU 上的接口库**

由 Rebellions 维护的 Optimum 硬件后端库：在 HuggingFace Transformers/Diffusers 与 RBLN NPU（ATOM、Rebel100）之间提供接口，把模型类替换为 RBLN 对应类后首次运行即经 RBLN SDK 编译，支持单/多 NPU 推理；也可用 optimum-rbln-cli 预编译保存产物，后续直接加载免重编译。限制：运行所需的 rebel-compiler 库仅向获批用户提供。通过 pip 或源码（uv）安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- HuggingFace pipeline 类的直接替换式 API（RBLN 对应类）
- optimum-rbln-cli 预编译与产物加载、类与配置查看
- 单/多 NPU 推理支持（--num_devices）
- 维护经验证的模型与任务清单，其他模型可少量修改适配

## 适用场景

- 把已有的 Transformers/Diffusers 代码迁移到 RBLN NPU 上运行
- 提前编译模型产物并部署到多 NPU 环境
- 查看可用的 RBLN 类及其 rbln_config 配置项

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L10: 🤗 Optimum RBLN provides an interface between HuggingFace libraries (Transformers, Diffusers) and RBLN NPUs, includi
> L12: This library enables seamless integration between the HuggingFace ecosystem and RBLN NPUs through a comprehensive t

## 星数曲线

```mermaid
xychart-beta
    title "RBLN-SW/optimum-rbln 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-28 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `63742aaf6db0` · [字段定义](../../DATASET.md)*
