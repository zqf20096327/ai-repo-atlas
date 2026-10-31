# zenml-io/vscode-zenml

⭐ 21 · TypeScript · Apache-2.0 · 推送 2026-10-17 · [GitHub](https://github.com/zenml-io/vscode-zenml) · [官网](https://marketplace.visualstudio.com/items?itemName=ZenML.zenml-vscode) · 组织维护

**ZenML 的 VSCode 扩展：在 IDE 内管理 MLOps 栈与流水线**

由 ZenML 团队（zenml-io）维护的 Visual Studio Code 扩展，将 ZenML MLOps 框架的环境状态映射到 IDE 中：提供 Server、Projects、Stacks、Pipeline Runs 与 Models 视图，支持栈/组件的注册更新删除、流水线运行的监控与 DAG 可视化渲染。内置 LSP 服务器与 watchdog 实现与本地 ZenML 环境的实时同步。要求本地 Python 环境已安装 ZenML（兼容 0.83.x）且 Python 3.8+。默认收集匿名使用分析，可通过设置关闭。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Activity Bar 中提供 Server/Projects/Stacks/Pipeline Runs/Models 视图
- 流水线运行的 DAG 可视化（平移、缩放、节点详情、跳转 dashboard）
- 通过 LSP 服务器与 watchdog 实时同步 ZenML 环境状态
- 状态栏显示并快速切换当前 stack、project 与连接状态

## 适用场景

- 在 VSCode 内直接管理和切换 ZenML 项目与栈
- 监控流水线运行并可视化查看 DAG 结构与产物
- 浏览模型版本、产物、标签与元数据

## 场景标签

`MLOps` · 领域:训练与推理

## 证据(README 行号)

> L5: The ZenML VSCode extension seamlessly integrates with ZenML to enhance your MLOps workflow within VSCode. It is desi
> L9: - **Server, Projects, Stacks, and Pipeline Runs Views**: Interact directly with ML stacks, pipeline runs, and server

## 星数曲线

```mermaid
xychart-beta
    title "zenml-io/vscode-zenml 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `c7f3c951b243` · [字段定义](../../DATASET.md)*
