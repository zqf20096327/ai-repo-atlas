# Bellman281/esp32-tinyLLM

⭐ 48 · Rust · Apache-2.0 · 推送 2026-08-20 · [GitHub](https://github.com/Bellman281/esp32-tinyLLM) · 个人维护

**在 ESP32-S3 上运行 28.9M 参数小语言模型的 Rust 推理引擎**

将 C 实现的 28.9M 参数 PLE TinyLM 逐函数移植为 Rust 的嵌入式推理引擎，运行于 512KB SRAM 的 ESP32-S3：约 25M 参数存于 flash 映射的 Per-Layer Embedding 表，其余 4-bit 量化。设备端以 10.50 tok/s 生成短篇儿童故事（--fast-mspi 达 10.89 tok/s），输出与 C 版逐字节一致，由板上 token 摘要验证。模型不能回答问题或遵循指令。提供无硬件的本机 cargo test/CLI 路径与设备刷写脚本，含 16 个测试文件、38 个测试。Apache 2.0 许可。

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

- 28.9M 参数模型运行在 512KB SRAM 的 ESP32-S3 上（10.50 tok/s）
- PLE 表 flash 映射 + 4-bit 量化使参数装入微控制器
- Rust 与 C 版逐字节一致输出，由板上摘要与 host 端重算验证
- 无硬件即可运行：cargo test、本机 CLI 对话、双引擎基准

## 适用场景

- 在微控制器上运行量化小语言模型做文本生成实验
- 验证嵌入式推理优化不改变模型计算结果
- 复现 C vs Rust 嵌入式推理性能基准

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L3: **A 28.9M-parameter language model running on an $8 microcontroller — rewritten in Rust,
> L8: magnitude down) and the rest are 4-bit quantized. It writes short children's stories at
> L21: |**Rust**|4.0|27.1|6.5|7.9|49.7|**95.2**|10.50|

## 星数曲线

```mermaid
xychart-beta
    title "Bellman281/esp32-tinyLLM 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 46 --> 49
    line [47, 48, 48]
```

2026-10-18 47 → 2026-10-31 48（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1ecaa09cf459` · [字段定义](../../DATASET.md)*
