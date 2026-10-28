# MaincodeHQ/from-tin-to-tokens

⭐ 30 · CC-BY-4.0 · 推送 2026-08-13 · [GitHub](https://github.com/MaincodeHQ/from-tin-to-tokens) · 组织维护

**用 Rust 从零构建 LLM 推理栈的免费教材**

由 Maincode 的 Dave Lemphers 撰写的免费教材，讲解推理栈工程全链路：从手写 ioctl 结构的驱动接口，到服务数千并发用户的 HTTP 端点，覆盖 attention 内核、分页 KV cache、调度器、多 GPU 集合通信、量化流水线与正确性验证方法。概念先于实现组织内容。以 PDF 电子书形式通过 releases 页面按编号版本发放，勘误集中记录于 ERROTA.md 并并入下版；配套课程与参考实现尚未发布。采用 CC BY 4.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | CC-BY-4.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 覆盖驱动接口到 HTTP 端点的完整推理栈工程内容
- 包含 attention 内核、分页 KV cache、调度器、多 GPU collectives、量化流水线等主题
- 每个数字注明条件、每项测量注明硬件，支持可复现勘误
- CC BY 4.0 许可，可自由阅读、分享与教学

## 适用场景

- 系统学习 LLM 推理栈各层组件的工程原理
- GPU/系统编程方向开发者理解推理内核与调度设计
- 作为课程或参考实现的配套教材阅读

## 场景标签

`教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: Building an LLM Inference Stack from Scratch in Rust.
> L5: A free textbook on inference-stack engineering. It covers the whole stack, from the driver interface where you write

## 星数曲线

```mermaid
xychart-beta
    title "MaincodeHQ/from-tin-to-tokens 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 28 --> 31
    line [29, 30, 30]
```

2026-10-18 29 → 2026-10-28 30（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a0de6415737c` · [字段定义](../../DATASET.md)*
