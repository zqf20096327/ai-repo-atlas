# bentoml/BentoVLLM

⭐ 175 · Python · Apache-2.0 · 推送 2026-10-13 · [GitHub](https://github.com/bentoml/BentoVLLM) · 组织维护

**BentoML 官方 vLLM 部署示例集：自托管开源 LLM 服务**

BentoML 组织维护的示例项目集合，演示如何用 vLLM 推理引擎通过 BentoML 服务化部署 25 个开源大模型（Llama、Qwen、DeepSeek、gpt-oss 等）。每个模型目录包含为 BentoML Service 添加 OpenAI 兼容端点的代码，支持 vLLM 扩展参数（如 guided_json），可本地 bentoml serve 运行或部署到 BentoCloud；也可作为自定义模型、推理逻辑与 vLLM 选项的改造基础。面向希望自托管 LLM 的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 25 个开源 LLM 的 BentoML+vLLM 服务化示例
- 每个 Service 提供 OpenAI 兼容端点并支持 vLLM 扩展参数
- 支持部署到 BentoCloud 或生成 OCI 镜像自建基础设施

## 适用场景

- 用 BentoML+vLLM 自托管 LLM 并获得 OpenAI 兼容 API
- 参考示例代码定制推理逻辑或 vLLM 选项
- 将 LLM 服务部署到 BentoCloud 管理

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L3: This repository contains a group of BentoML example projects, showing you how to serve and deploy open-source Large 
> L5: 💡 You can use these examples as bases for advanced code customization, such as custom model, inference logic or vLLM

## 星数曲线

```mermaid
xychart-beta
    title "bentoml/BentoVLLM 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 174 --> 176
    line [175, 175]
```

2026-10-18 175 → 2026-10-25 175（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `c398cf78b3a2` · [字段定义](../../DATASET.md)*
