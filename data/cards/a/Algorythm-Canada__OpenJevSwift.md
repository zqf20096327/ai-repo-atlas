# Algorythm-Canada/OpenJevSwift

⭐ 10 · Swift · Apache-2.0 · 推送 2026-11-18 · [GitHub](https://github.com/Algorythm-Canada/OpenJevSwift) · [官网](https://algorythm-canada.github.io/OpenJevSwift/) · 组织维护 · 中文 README

**macOS/iOS 本地运行的 Jev 兼容型判定服务器（Swift 原生）**

OpenJev 的原生 Swift 实现：对文本发起类型化问题（yes/no、选项、打分），从模型概率直接读取答案而非生成文本，答案不会越出 schema。一个 openjev 二进制在 Mac 上提供 Jev 兼容 HTTP API（上游线协议一致），支持 Verdict/Laya（Core ML）与 DiffusionGemma/JevK5（MLX）四种后端，也可作为 Swift 库嵌入 iPhone/Mac 应用内运行。面向需要在设备本地获得判定结果的 Swift 开发者与 Mac 用户；目前仅覆盖 Apple silicon 平台，Linux 仅编译核心与服务用于测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 从模型概率读取 noul/choice/score 三类答案，带每选项概率与置信度
- 与上游 Jev 线协议逐字节一致，TypeSafe SDK 无需改动即可对接
- 四种后端（Verdict/Laya/DiffusionGemma/JevK5）由同一二进制提供服务
- 提供 iPhone 分诊示例应用，输入同时实时作答

## 适用场景

- 在 Mac 本地部署 Jev 兼容 API 而不搭建 Python 环境
- 在 iOS 应用内做客户消息优先级、分派团队与情绪打分
- 依据兼容性报告核对与上游判定结果的一致性

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L9: locally: on your Mac behind a Jev-compatible HTTP API, or inside your own iPhone or Mac app. It is
> L15: Jev-compatible "System One" decision server. Send it a state and typed questions (`noul`,
> L19: DiffusionGemma 26B-A4B or JevK5 on MLX, or Verdict or Laya on Core ML, on a Mac, with upstream's

## 星数曲线

```mermaid
xychart-beta
    title "Algorythm-Canada/OpenJevSwift 星数(近 2 点)"
    x-axis ["2026-10-21", "2026-11-23"]
    y-axis "stars" 9 --> 11
    line [10, 10]
```

2026-10-21 10 → 2026-11-23 10（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-20 · 置信度 high · 依据 README sha `6de86b83ccfe` · [字段定义](../../DATASET.md)*
