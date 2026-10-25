# Emmimal/context-compiler

⭐ 63 · Python · MIT · 推送 2026-08-29 · [GitHub](https://github.com/Emmimal/context-compiler) · [官网](https://towardsdatascience.com/author/emmimalp-alexander/) · 个人维护

**纯 Python 仓库可达性分析与骨架化层：为编码 agent 精简上下文**

面向编码 agent 的上下文编译库：在请求发送到 API 之前，从目标文件出发追踪导入与调用点构建近似依赖图（可配置跳数），用 ast.NodeTransformer 剥离函数体保留签名与文档字符串，将仓库文件分为三级（目标文件全文、可达依赖骨架、其余排除），并输出相对全仓转储的 token 缩减统计。仅依赖标准库（ast/pathlib/dataclasses），需 Python 3.9+。提供 5 个示例、CLI 基准脚本与 14 个单元测试。已知限制：裸名解析存在动态分发、事件装饰器、命名冲突三类盲点；token 估算用字符÷4 启发式，无跨次缓存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三趟流程：符号可达性解析 → AST 骨架化 → 三级上下文装配，一次 compile() 调用完成
- 零第三方依赖，仅标准库，附带 5 个可运行示例与 14 个测试
- 输出 token 缩减统计（自基准 69.4%，外部仓库 74.3%）
- 文档明示三类可复现盲点与适用/不适用场景

## 适用场景

- 多文件 agent 任务中只把与目标文件相关的代码送入模型
- 在有限上下文预算下压缩发送给 LLM 的仓库内容
- 为编码 agent 管道生成骨架化的 repo map 替代全仓转储

## 场景标签

 · 领域:开发者工具/LLM 上下文工程

## 证据(README 行号)

> L3: A pure-Python reachability and skeletonization layer that decides what a coding agent actually sees before a request
> L7: Most coding agents build a "repo map" — file paths and source concatenated together — and send the whole thing to th

## 星数曲线

```mermaid
xychart-beta
    title "Emmimal/context-compiler 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-25 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9740729869c4` · [字段定义](../../DATASET.md)*
