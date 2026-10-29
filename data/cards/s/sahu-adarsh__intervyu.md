# sahu-adarsh/intervyu

⭐ 21 · TypeScript · MIT · 推送 2026-06-29 · [GitHub](https://github.com/sahu-adarsh/intervyu) · [官网](https://intervyu.io) · 个人维护

**AI 语音模拟面试平台：语音对答、在线编程与评分报告**

面向求职者的模拟面试 Web 平台：用户与名为 Neerja 的 AI 面试官进行实时语音对话，可在 Monaco 编辑器中现场解编程题（沙盒执行测试），上传简历后可被针对性追问，结束后输出 5 维度评分、HIRE/NO_HIRE 判定与百分位对标，共 8 种面试类型。技术栈为 Next.js 15 + FastAPI，LLM 用 Claude Haiku 4.5（AWS Bedrock converse_stream），STT 用 Deepgram Nova-2，TTS 用 Azure Speech，前端 Silero VAD 做语音活动检测，Supabase 提供认证与数据库。自部署需 AWS/Deepgram/Azure/Supabase 多项凭据，语音端到端延迟约 1.7–4.0 秒。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AI 面试官实时语音对答，speech_end 到首音频约 1.7s
- Monaco 编辑器内现场解编程题并沙盒执行测试
- 8 种面试类型（Google/Amazon/Microsoft SDE、云架构师、CV 追问等）
- 5 维度评分 + HIRE/NO_HIRE + 百分位对标的绩效报告

## 适用场景

- 我求职前想练真实的语音技术面试，体验追问与临场压力
- 我想在带测试执行的编辑器里练编程题并即时看结果
- 我想上传简历，模拟被深挖项目经历的追问
- 面试后我想拿到维度化评分和是否会被录用的判定

## 场景标签

`语音 Agent` · 领域:对话与助手

## 证据(README 行号)

> L3: ### AI-powered mock interview platform for voice interviews, live coding, and real-time performance feedback.
> L19: intervyu.io puts you in a real interview. You speak, and an AI interviewer named Neerja listens, responds, and adap
> L97: |**AI / ML**|Claude Haiku 4.5 (Anthropic API), Deepgram Nova-2 (STT), Azure Speech `en-IN-NeerjaNeural` (TTS), Sile

## 星数曲线

```mermaid
xychart-beta
    title "sahu-adarsh/intervyu 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `7f1890bf935f` · [字段定义](../../DATASET.md)*
