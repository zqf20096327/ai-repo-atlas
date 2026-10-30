# gokeshenzhen/gen-tb-skill

⭐ 27 · Python · Apache-2.0 · 推送 2026-07-14 · [GitHub](https://github.com/gokeshenzhen/gen-tb-skill) · 个人维护

**从 IP 规格与寄存器表生成 UVM 测试平台脚手架的 agent 技能**

一个运行于 Claude Code 与 Codex CLI 的 agent skill：读取 IP 规格文档（docx/pdf/md）与寄存器表（xlsx/csv/md/IP-XACT），经 7 阶段流水线生成完整可运行的 UVM 测试平台脚手架。内置 APB、AHB-Lite、AXI4-Lite 三类总线，其他单通道请求/响应总线走通用回退路径。面向两类用户：DV 工程师用 UVM sequence 驱动，DE 工程师通过 tb_api:: 任务型 BFM 使用而无需 UVM 经验。README 自述处于 pre-alpha 阶段，AXI4 full 不在 v1 范围内。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从规格文档与寄存器表（含 IP-XACT）生成 UVM 测试平台脚手架
- 内置 APB/AHB-Lite/AXI4-Lite 总线，其他单通道总线由约束式子代理推断回退生成
- 双角色设计：DV 走 UVM sequence，DE 走无 UVM 门槛的 tb_api:: 任务 BFM
- 支持 VCS/Questa/Xcelium 仿真器，附本地回归测试夹具与评测脚本

## 适用场景

- DV 工程师从 IP 规格快速搭建可运行的 UVM 验证环境
- DE 工程师不写 UVM 代码也能用任务接口驱动测试平台
- 对 I2C/SPI 等自定义总线生成结构一致的验证脚手架

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: A skill that generates a complete UVM testbench scaffold for a single IP
> L7: (xlsx / csv / md / IP-XACT). Runs under both **Claude Code** and

## 星数曲线

```mermaid
xychart-beta
    title "gokeshenzhen/gen-tb-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 26 --> 28
    line [27, 27]
```

2026-10-18 27 → 2026-10-30 27（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `83eca53324b4` · [字段定义](../../DATASET.md)*
