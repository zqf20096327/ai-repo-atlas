# QwertyMcQwertz/monkeys-with-typewriters

⭐ 49 · C++ · 推送 2026-02-19 · [GitHub](https://github.com/QwertyMcQwertz/monkeys-with-typewriters) · [官网](https://monkeyswithtypewriters.com) · 个人维护

**运行在 $3 微控制器上的戏仿式文本生成平台**

在 WeMos D1 Mini（ESP8266）上运行的固件项目，自称『完整 AI 平台』：16 个 API 端点覆盖生成、流式、多 agent、RAG、思维链、嵌入、微调、护栏、工具调用与多模态，并提供 OpenAI 兼容的 /v1/chat/completions 接口。其真实机制是 342 词表加 random() 随机拼接，不含任何机器学习；README 明示该项目对 AI 营销进行戏仿（『It is. The results are real.』），输出为随机企业话术文本，作者声明不可用于实际生成有意义内容。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ESP8266 上提供 16 个 API 端点，含 OpenAI 兼容 chat/completions 接口
- 模型为 342 词表 + random() 随机拼接，无机器学习成分，无训练数据
- 多 agent、RAG、思维链等特性均为同一随机函数的不同调用方式
- 按集群购买更多 $3 微控制器即可横向扩展

## 适用场景

- 作为 AI 行业营销话术的戏仿与批评性作品阅读
- 在微控制器上运行一个输出随机文本的 OpenAI 兼容 API 服务
- 极低成本演示流式输出、多端点服务等接口形态

## 场景标签

 · 领域:边缘计算/AI 戏仿

## 证据(README 行号)

> L24: MWT-1 is a breakthrough text generation platform that achieves what the $150 billion AI industry has been promising
> L28: The model is a 342-token vocabulary and a call to `random()`. That's the architecture. The rest is API endpoints.
> L155: POST /v1/chat/completions

## 星数曲线

```mermaid
xychart-beta
    title "QwertyMcQwertz/monkeys-with-typewriters 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 48 --> 50
    line [49, 49]
```

2026-10-18 49 → 2026-10-29 49（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `08295f5e9788` · [字段定义](../../DATASET.md)*
