# CharlesPikachu/FreeGPTHub

⭐ 68 · Python · Apache-2.0 · 推送 2026-07-29 · [GitHub](https://github.com/CharlesPikachu/FreeGPTHub) · [官网](https://freegpthub.readthedocs.io/en/latest/) · 个人维护 · 中文 README

**免费统一 GPT API 网关库，聚合九家大模型端点**

提供统一 Python 接口调用多家 LLM/MLLM 端点的库：通过 ChatRequest 与各 provider 专属的 *Endpoints 客户端发送请求，send() 返回统一的 ChatResponse。当前支持阿里通义千问、百度文心、DeepSeek、字节豆包、讯飞星火、MiniMax、魔搭社区、OpenAI ChatGPT、智谱九类端点，并按 I/O 模态（T2T/TI2T 等）路由请求。免费 API 依赖公开网络抓取的端点与项目账号免费额度，速度稳定性不保证；使用前需关注微信公众号并私信获取加密的 key/aes_gem_key。项目仅限非商业用途，禁止任何商业化使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 统一 ChatRequest/ChatResponse 接口覆盖 9 家模型端点，切换 provider 只需更换客户端类
- 按 I/O 模态（TEXT/IMAGE/AUDIO/VIDEO，T2T/TI2T 标签）路由请求
- EndpointRegistry 支持列出全部端点、按 IO 类型与 provider/model 检索
- 支持视觉请求（bytes/url/(bytes,mime) 图像输入）

## 适用场景

- 不购买各平台付费额度，用统一接口调用多家大模型
- 在同一代码里快速切换 DeepSeek、通义千问、豆包等 provider 做对比
- 个人学习或教学演示中搭建多模型调用示例

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L92: FreeGPTHub provides a unified Python interface to call multiple LLM / MLLM endpoints via provider-specific `*Endpoi
> L36: A truly free, unified GPT API gateway—unlike “fake-free” alternatives that hide paywalls behind quotas, trials, or 

## 星数曲线

```mermaid
xychart-beta
    title "CharlesPikachu/FreeGPTHub 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-25 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `120877fb1786` · [字段定义](../../DATASET.md)*
