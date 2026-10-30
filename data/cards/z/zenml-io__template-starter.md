# zenml-io/template-starter

⭐ 21 · Python · Apache-2.0 · 推送 2026-01-20 · [GitHub](https://github.com/zenml-io/template-starter) · 组织维护

**ZenML 起步项目模板：生成含步骤与流水线的初始工程**

基于 Copier 与 Jinja2 模板的 ZenML 项目脚手架：通过 zenml init --template 或直接调用 copier 从本仓库生成一个简单 ZenML 项目，内含步骤（steps）、流水线（pipelines）、stack 配置等资源。使用前需安装 ZenML 及其 templates extras（pip install "zenml[templates]"）。重复运行命令可更新已生成项目的参数，也可用 copier -wf 跳过提示覆盖全部文件。面向使用 ZenML 做 MLOps 的开发团队。

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

- 提供 steps、pipelines、stack 配置等项目起步资源
- 通过 zenml init --template 一条命令生成项目
- 底层使用 Copier 与 Jinja2 模板，可直接调用 copier 生成
- 重复运行命令可更新已生成项目的参数或覆盖文件

## 适用场景

- 快速搭建第一个 ZenML MLOps 项目
- 以模板为起点编写自己的机器学习流水线
- 团队统一起步工程结构与配置

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains a starter template from which a simple ZenML project
> L4: can be generated easily. It contains a collection of steps, pipelines, stack configurations and

## 星数曲线

```mermaid
xychart-beta
    title "zenml-io/template-starter 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `34a0302810bc` · [字段定义](../../DATASET.md)*
