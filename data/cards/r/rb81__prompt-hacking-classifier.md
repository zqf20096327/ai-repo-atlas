# rb81/prompt-hacking-classifier

⭐ 20 · Python · MIT · 推送 2026-06-15 · [GitHub](https://github.com/rb81/prompt-hacking-classifier) · 个人维护

**检测提示注入/越狱的小型自托管模型防护方案**

提供两个分类器提示词（完整版 88 行与轻量版 22 行），配合自托管小模型作为前置安全防护：将用户输入填入提示词交给防护模型，返回 true/false 判定是否为恶意输入，由应用逻辑决定后续处理。在 35 个模型、161 个测试用例上做了三组对照实验，最高 F1 超过 0.97，并给出推荐模型列表与测试脚本（Ollama 运行）。限制：仅覆盖英文文本攻击，属纵深防御中的一层。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 完整版与轻量版两个分类器提示词，{{USER_MESSAGE}} 占位注入用户输入
- 35 模型 × 161 测试用例的三组对照实验（完整/轻量/无提示词）
- 检测系统提示词提取、指令覆盖、社会工程、内存转储、伪权威等攻击
- 测试脚本支持中断续跑与 thinking 模型输出解析

## 适用场景

- 在我的 LLM 应用前加一层便宜的自托管恶意输入分类
- 选择适合速度/准确度权衡的防护小模型
- 复现提示词对模型攻击抵抗力的对照实验

## 场景标签

`提示工程` `网络安全` · 领域:Agent 开发

## 证据(README 行号)

> L3: A simple prompt-based approach to detecting prompt injection and jailbreaking attempts using small, self-hosted lang
> L11: This project explores whether **smaller, self-hosted models** can serve as cheap, fast, portable safety guards when
> L71: │ User Input  │────▶│  Guard Model     │────▶│ true/false  │

## 星数曲线

```mermaid
xychart-beta
    title "rb81/prompt-hacking-classifier 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 19 --> 21
    line [20, 20]
```

2026-10-18 20 → 2026-10-29 20（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a8a2c0ea9a3d` · [字段定义](../../DATASET.md)*
