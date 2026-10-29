# lawrencewzen/pi-vlm-proxy

⭐ 29 · TypeScript · MIT · 推送 2026-08-03 · [GitHub](https://github.com/lawrencewzen/pi-vlm-proxy) · 个人维护 · 中文 README

**pi 编程助手的视觉代理扩展：让纯文本模型委托多模态模型识图**

面向 pi coding agent 的扩展：为主模型添加 describe_image 工具，图片先发往用户指定的任意 OpenAI 兼容多模态模型转成文字，再交回主模型继续对话。零厂商硬编码，模型即地址+Key+模型 ID 三项配置；主模型本身支持视觉时自动隐藏工具、原生透传，无额外 API 调用。支持环境变量引用密钥、配置权限 600、原子写入。以 npm 包经 pi install 安装，61 项单元测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- describe_image 工具将图片委托给任意 OpenAI 兼容多模态模型
- 能力感知：主模型支持视觉时自动隐藏工具走原生透传
- 零厂商硬编码，密钥支持 $ENV_NAME 引用且展示脱敏
- path 与 base64 两种传图方式，10MB 本地体积上限

## 适用场景

- 继续用 DeepSeek 等纯文本主模型，同时能处理截图和图片
- 在多个多模态后端（火山 Ark、Qwen-VL、本地 vLLM 等）间切换视觉模型
- 粘贴截图让编码助手理解界面内容

## 场景标签

`编码 Agent` `多模态` · 领域:编码与开发

## 证据(README 行号)

> L5: 给 pi 用的视觉代理扩展 —— 把图片识别委托给任意 OpenAI 兼容的多模态模型
> L20: 本扩展给它加一个 `describe_image` 工具：图片先送到你指定的多模态模型那里转成文字，再交回主模型继续对话。**你不必为了看一张图就切换主模型。**
> L69: |🌐 **通吃 OpenAI 格式**|火山 Ark、阶跃 StepFun、OpenAI、通义 Qwen-VL、智谱 GLM、OpenRouter、硅基流动、本地 vLLM / Ollama / llama.cpp……|

## 星数曲线

```mermaid
xychart-beta
    title "lawrencewzen/pi-vlm-proxy 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-29 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `2d6d66a2d94a` · [字段定义](../../DATASET.md)*
