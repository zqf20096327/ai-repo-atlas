# tchivs/gsd-omp

⭐ 19 · JavaScript · MIT · 推送 2026-10-22 · [GitHub](https://github.com/tchivs/gsd-omp) · [官网](https://github.com/tchivs/gsd-omp#readme) · 个人维护 · 中文 README

**把 GSD 编排系统接入 Oh My Pi 的第三方宿主插件**

独立维护的 Oh My Pi（OMP）宿主插件，将 OMP 的扩展、命令、事件、任务与文件系统接口通过公开 Host-Integration SDK（协议版本 1）绑定到 GSD 可嵌入编排系统：注册 39 个核心斜杠命令与 gsd_invoke 工具，覆盖项目生命周期、阶段规划、执行验证、质量审计、发布等流程；在支持 Goal Mode 的宿主上映射可选目标状态。模型路由声明为 passive，OMP 为模型权威，插件不做按 agent 桥接。需 Node.js 24+ 与支持 ExtensionAPI 的 OMP，通过 npm 全局安装 tarball。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 注册 39 个核心斜杠命令与 gsd_invoke 结构化工具
- 通过 Host-Integration SDK 协议版本 1 绑定 OMP 原生接口
- 支持 Goal Mode 状态映射（宿主不支持时其余功能仍可用）
- 提供 install/uninstall/doctor/descriptor/update CLI 与多级 locale 解析

## 适用场景

- 在 Oh My Pi 中使用 GSD 的阶段规划与验证工作流
- 通过斜杠命令管理项目生命周期与质量审计
- 让 GSD 与 OMP 的会话、任务、上下文压缩机制协同运行

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L15: `gsd-omp` is an independently maintained Oh My Pi host plugin for the GSD Embeddable Orchestration System. It binds
> L65: The plugin also registers the `gsd_invoke` tool for structured access to the public `gsd-tools` CLI.

## 星数曲线

```mermaid
xychart-beta
    title "tchivs/gsd-omp 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 18 --> 20
    line [19, 19]
```

2026-10-18 19 → 2026-10-29 19（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `b4772f571bd3` · [字段定义](../../DATASET.md)*
