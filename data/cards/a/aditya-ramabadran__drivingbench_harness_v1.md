# aditya-ramabadran/drivingbench_harness_v1

⭐ 60 · Python · NOASSERTION · 推送 2026-09-26 · [GitHub](https://github.com/aditya-ramabadran/drivingbench_harness_v1) · [官网](https://drivingbench.com) · 个人维护

**让 LLM 通过 MCP 工具在封闭场地驾驶真实汽车的研究测试框架**

DrivingBench Harness 是研究软件：在 comma four 设备的 openpilot 上打补丁，把汽车暴露为一个 MCP 服务器 drivingbench_sandbox，提供 observe/set_motion/stop_now 三个工具，使 Codex、Claude Code、Cursor 等聊天应用中的语言模型能在停车场低速控制一辆受支持丰田汽车的转向、加速与刹车，全程需人类驾驶员脚踩刹车监督。带速度上限（默认 3 m/s，6 m/s 紧急切断）、指令过期等软件限制，并记录全部工具调用与遥测为可回放 trace，支持标注会话基准测试与 Hugging Face 上传。面向自动驾驶/LLM 研究者，仅限封闭场地使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MCP 服务器暴露 observe/set_motion/stop_now 三工具，任何支持 MCP 的聊天应用可接入
- 100 Hz 控制回路接管 openpilot 规划器，速度上限默认 3 m/s、6 m/s 紧急切断、指令过期机制
- 全部工具调用、遥测与图像记录为可回放 trace，支持标注会话基准测试
- 激活脚本逐项检查前置条件并保留回滚

## 适用场景

- 在封闭场地评测前沿 LLM 的实车驾驶能力
- 回放模型所见画面与决策 trace 做分析
- 把标注驾驶会话产物发布到 Hugging Face 数据集

## 场景标签

`模型评测` · 领域:评测与运维

## 证据(README 行号)

> L3: A small harness that lets a language model drive a real car at parking-lot
> L7: exposes the car to any chat app that speaks MCP (Codex, Claude Code, Cursor) as
> L151: measured steering and speed, and every tool call with its reason. To benchmark, start a

## 星数曲线

```mermaid
xychart-beta
    title "aditya-ramabadran/drivingbench_harness_v1 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-29"]
    y-axis "stars" 58 --> 61
    line [59, 60, 60]
```

2026-10-18 59 → 2026-10-29 60（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `6f3f6772ad4b` · [字段定义](../../DATASET.md)*
