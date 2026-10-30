# i-am-logger/pr4xis

⭐ 15 · Rust · NOASSERTION · 推送 2026-10-09 · [GitHub](https://github.com/i-am-logger/pr4xis) · [官网](https://pr4xis.dev) · 个人维护

**基于公理推导的确定性推理引擎，替代统计式生成**

以 Rust 编写的公理化智能引擎：不从训练数据预测，而是从被接受的公理推导结论，每条声明可追溯到证明路径。数学基础涵盖 Spencer-Brown《Laws of Form》、Heim 句法度量逻辑与应用范畴论，内置 182 个领域本体（含轨道力学、卡尔曼滤波、SLAM 等安全关键领域）。六项保证（可验证/确定性/可解释/诚实/一致/可组合）由 7,226 个测试逐一声明并通过完整性门禁强制分类。提供浏览器内运行的 demo（无服务器、无 GPU、无 API key），安装与 CLI 入口在 get-started 文档。许可为 CC BY-NC-SA 4.0（非商业）。定位为 LLM 的校验后端或长期知识库底座。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从公理推导结论而非统计预测，输出字节级确定
- 182 个领域本体，跨域连接经函子法则校验
- 7,226 个测试逐条声明其见证的保证，门禁脚本强制无遗漏
- 浏览器内完整运行 demo，无服务器/GPU/API key

## 适用场景

- 在安全关键工程（航天导航、传感器融合）中做可验证推理
- 作为生成式前端的确定性校验器，验证 LLM 输出的声明
- 维护长期增长且保持机器可校验的知识库

## 场景标签

`知识图谱` · 领域:知识与检索

## 证据(README 行号)

> L19: **pr4xis is a new kind of AI: axiomatic, not statistical.** Where LLMs predict the next token from training data, p
> L53: - **LLM verification** — pr4xis as a deterministic checker behind a generative front end. The LLM produces text; pr
> L31: Try it now: **pr4xis.dev** — runs entirely in the browser. No server, no GPU, no API key. If a query breaks, file a

## 星数曲线

```mermaid
xychart-beta
    title "i-am-logger/pr4xis 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `7800b23f7b22` · [字段定义](../../DATASET.md)*
