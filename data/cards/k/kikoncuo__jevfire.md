# kikoncuo/jevfire

⭐ 76 · JavaScript · MIT · 推送 2026-09-18 · [GitHub](https://github.com/kikoncuo/jevfire) · [官网](https://kikoncuo.github.io/jevfire/learn.html) · 个人维护

**为开发者提供基于 vLLM 的并行字段决策打分层**

JEVfire 是一个面向 LLM 推理的 HTTP 侧车组件：把多个独立的布尔/枚举决策字段批量送入 vLLM，利用模型已有的语言模型头对经验证的单 token 标签打分，选出各字段胜者后在代码层组装 JSON。不加载第二份模型、无需再训练，结构上保证输出字段与取值不越界（但不保证事实正确）。支持 1-64 字段、每字段最多 255 个选项；附三个浏览器游戏 demo（本地 Qwen 0.8B 经 WebLLM/WebGPU 运行）与可复现基准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 共享前缀下批量打分独立决策字段，官方基准 28 字段任务中位 496.9 ms（对照约束 JSON 生成 5113.1 ms）
- 复用预训练权重与 LM head 打分单 token 标签，无需再训练或第二模型
- 输出结构由 schema 约束：代码只组装已声明的键与允许值
- 提供 Super Mario / 赛车 / 村庄生存三个浏览器游戏 agent 示例

## 适用场景

- 游戏 agent 需要在共享上下文下高频做出多个有限选项决策时降低延迟
- 替代逐 token 生成约束 JSON 的方式获取结构化字段决策
- 复现或验证批量标签打分与约束解码的延迟对比实验

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: JEVfire assigns typed variables from finite choices, batching independent fields
> L4: through vLLM for parallel execution and reuse of their shared instruction/context
> L122: vLLM owns CUDA execution and KV state. JEVfire is a lightweight HTTP sidecar;

## 星数曲线

```mermaid
xychart-beta
    title "kikoncuo/jevfire 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-25"]
    y-axis "stars" 74 --> 77
    line [75, 76, 76]
```

2026-10-18 75 → 2026-10-25 76（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bdd68a699026` · [字段定义](../../DATASET.md)*
