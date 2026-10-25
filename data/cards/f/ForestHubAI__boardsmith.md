# ForestHubAI/boardsmith

⭐ 37 · Python · AGPL-3.0 · 推送 2026-03-11 · [GitHub](https://github.com/ForestHubAI/boardsmith) · [官网](https://github.com/ForestHubAI/boardsmith#quick-start) · 组织维护

**从自然语言描述生成 KiCad 电路、BOM、固件与 Gerber 的工具**

面向硬件开发者的 Python 命令行工具：输入自然语言电路描述（如 ESP32 + BME280），经 9 阶段合成管线与 11 项约束检查（电压兼容、I2C 地址冲突、上拉值、功耗预算、ERC 等），输出可直接在 KiCad 打开的接线原理图、含厂商料号的 BOM、Arduino/ESP-IDF 固件及 JLCPCB 兼容 Gerber。支持 212 个经过验证的元器件，目标硬件覆盖 ESP32、RP2040（Stable）与 STM32（Beta）。LLM 可选：--no-llm 模式下用内置知识库离线确定性运行，无需 API key；接入 LLM 后可通过 ERCAgent 自动修复 ERC 违规、对既有原理图做增量修改与语义验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 9 阶段合成管线与 11 项约束检查，产出计算值而非模板
- --no-llm 离线确定性模式，无需 API key 与网络
- ERCAgent 读取真实 KiCad ERC 输出并自动打补丁修复（上限 5 次迭代）
- boardsmith modify 支持对既有 KiCad 原理图做增量补丁，写入前创建备份

## 适用场景

- 用一句话描述快速生成可制造的 ESP32/RP2040 原型电路与固件
- 离线浏览 212 个已验证元器件的电气参数与初始化时序
- 对已有 KiCad 原理图做增量修改并自动通过 ERC 验证

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L30: **boardsmith treats circuit design like compilation.** You describe what you want in plain English. A 9-stage synth
> L58: **Schematic** (`schematic.kicad_sch`) — Opens directly in KiCad. Not a template — an actual wired schematic with co
> L98: `--no-llm` runs the full pipeline deterministically — no API key, no network, same output every time. With an LLM, 

## 星数曲线

```mermaid
xychart-beta
    title "ForestHubAI/boardsmith 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-24", "2026-10-25"]
    y-axis "stars" 35 --> 38
    line [36, 37, 37]
```

2026-10-18 36 → 2026-10-25 37（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1a7c2b55e232` · [字段定义](../../DATASET.md)*
