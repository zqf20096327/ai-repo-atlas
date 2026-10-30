# ardoco/magika

⭐ 16 · Java · Apache-2.0 · 推送 2026-10-20 · [GitHub](https://github.com/ardoco/magika) · 组织维护

**Google Magika 文件类型识别工具的 Java 库封装**

将 Google Magika 的文件类型检测能力以 Java 依赖库形式提供：内置 ONNX 格式的深度学习分类模型（对应 google/magika v0.6.0），通过简单 API 对文件内容进行识别，识别在毫秒级完成、模型体积仅数 MB 且可在单 CPU 上运行。定位为 Maven Central 上的项目依赖而非独立工具，README 明确建议需要 CLI 的用户直接使用原版 google/magika。当前版本不做 polyglot 文件检测，采用 Apache 2.0 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Magika ONNX 分类模型（v0.6.0）的 Java API
- 模型体积数 MB，可在单 CPU 上毫秒级识别
- 发布于 Maven Central，作为依赖引入

## 适用场景

- 在 Java 项目中按文件内容识别类型/MIME
- 对上传文件做内容策略路由前的类型判定
- 替代基于扩展名的文件类型判断

## 场景标签

 · 领域:文件检测/开发库

## 证据(README 行号)

> L6: > Magika is a novel AI powered file type detection tool that relies on the recent advance of deep learning to provid
> L17: We provide a simple API to the ONNX model for classification (v0.6.0).

## 星数曲线

```mermaid
xychart-beta
    title "ardoco/magika 星数(近 2 点)"
    x-axis ["2026-10-22", "2026-10-30"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-22 16 → 2026-10-30 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `1533f0dd730a` · [字段定义](../../DATASET.md)*
