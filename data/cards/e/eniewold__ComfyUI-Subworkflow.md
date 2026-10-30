# eniewold/ComfyUI-Subworkflow

⭐ 15 · Python · GPL-3.0 · 推送 2026-08-20 · [GitHub](https://github.com/eniewold/ComfyUI-Subworkflow) · 个人维护

**ComfyUI 自定义节点集：把工作流封装为可复用子工作流节点**

为 ComfyUI 添加可复用工作流边界的扩展：通过 Subworkflow Input/Output 标记输入输出边界，让一个工作流可被另一个工作流通过单个 Subworkflow 节点加载执行，输入输出槽由内部工作流推断。支持从本地文件或 URL 加载，提供 Modifier 节点解决循环引用问题，同一工作流可不加修改地独立运行或作为内部工作流。安装方式为 ComfyUI Manager 或 git clone 到 custom_nodes 目录，无额外 Python 依赖。作者声明为早期版本，可能存在 bug 与破坏性变更；测试于 ComfyUI 0.18.2。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Subworkflow 节点在执行时将内部工作流展开为当前 prompt
- 从本地 workflows 目录或 http/https URL 加载内部工作流
- Modifier/Modifier Source 节点解决输出修改回传的循环引用
- 同一工作流可独立运行或作为子工作流复用而无需修改

## 适用场景

- 跨多个工作流复用提示词、采样器或解码链
- 把模型专属流程封装为少量命名输入输出
- 用已验证的底层工作流组装高层工作流

## 场景标签

`工作流自动化` `图像生成` · 领域:效率与自动化

## 证据(README 行号)

> L3: ComfyUI-Subworkflow adds reusable workflow boundaries to ComfyUI. It lets one workflow expose named inputs and outpu
> L9: To control the workflow boundaries, this extension adds several custom nodes: `Subworkflow`, `Subworkflow Input`, an

## 星数曲线

```mermaid
xychart-beta
    title "eniewold/ComfyUI-Subworkflow 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `6c2a2e3b6c92` · [字段定义](../../DATASET.md)*
