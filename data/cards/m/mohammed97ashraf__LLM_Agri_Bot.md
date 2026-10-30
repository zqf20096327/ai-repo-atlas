# mohammed97ashraf/LLM_Agri_Bot

⭐ 56 · Python · MIT · 推送 2026-06-21 · [GitHub](https://github.com/mohammed97ashraf/LLM_Agri_Bot) · [官网](https://llm-agri-bot.onrender.com/) · 个人维护

**面向印度农民的农业问答聊天机器人（文本/语音/图像）**

基于 Flask 的 Web 农业聊天机器人，面向印度农民提供作物种植、病虫害、土壤健康、天气与政府补贴政策咨询。支持文本对话、上传作物照片由视觉模型诊断病虫害与缺素、英语/印地语/Hinglish 语音输入（Groq Whisper）与语音播报（Orpheus TTS）。文本用 gpt-oss-120b、视觉用 llama-4-scout，均经 Groq API 调用；会话记忆存 Redis 并可回退内存，带提示前缀缓存。需 Groq API key，可用 uv 本地运行或 Docker/Render 部署。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本、语音（STT/TTS）、图像三种交互方式的农业问答
- 作物照片上传后由视觉 LLM 诊断病害、虫害与缺素
- Redis 会话记忆（内存自动回退）与提示前缀缓存
- 英语/印地语/Hinglish 多语言响应

## 适用场景

- 农民用手机以语音或拍照方式咨询作物问题
- 查询政府农业补贴与政策信息
- 获取病虫害防治与土壤健康建议

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L14: An AI-powered agriculture chatbot that helps Indian farmers with crop advice, pest control, soil health, weather, a

## 星数曲线

```mermaid
xychart-beta
    title "mohammed97ashraf/LLM_Agri_Bot 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 55 --> 57
    line [56, 56]
```

2026-10-18 56 → 2026-10-30 56（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `bab190817545` · [字段定义](../../DATASET.md)*
