# bobby-sheng/aitestmind

⭐ 67 · TypeScript · NOASSERTION · 推送 2026-06-22 · [GitHub](https://github.com/bobby-sheng/aitestmind) · 个人维护 · 中文 README

**AI 驱动的可视化 API 测试编排平台，自然语言生成测试用例**

面向测试工程师和开发者的 Web 端 API 测试平台（Next.js + Node.js + Python/FastAPI + SQLite）：三种采集方式（Playwright 浏览器录制、HAR 导入、mitmproxy 代理）自动识别 API 并生成 Schema；画布拖拽编排测试流程，支持断言、变量提取与串并行执行；用自然语言描述需求即可由 LLM 从 API 仓库生成测试用例，支持 OpenAI/DeepSeek/Claude/文心/通义/智谱/Ollama 等提供商。采用非商业使用协议，商业使用需联系作者获取授权。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三种 API 采集模式：Playwright 录制 / HAR 导入 / mitmproxy 代理（支持移动 App、小程序流量）
- 拖拽式可视化编排，支持断言、变量传递、并发节点与实时执行监控
- 自然语言生成测试用例，支持 7 家 AI 提供商（含 Ollama 本地部署）
- SSE 实时仪表盘、节点级日志、失败重试与执行历史

## 适用场景

- 我在网页或 App 上操作一遍，自动采集 API 建成接口仓库
- 用一句话描述场景，让 AI 自动生成接口测试和 E2E 流程用例
- 把 API 测试接入 CI/CD 流水线，实时看执行结果

## 场景标签

 · 领域:软件开发/测试工具

## 证据(README 行号)

> L96: 🎬 AI 智能采集  ──▶  🎨 可视化编排  ──▶  🤖 AI 生成用例  ──▶  ✅ 测试完成
> L118: #### 3️⃣ **AI 生成用例** - 自然语言秒变测试
> L161: > **完整工作流**: 🎬 采集 API → 🎨 编排流程 → 🤖 AI 生成 → ✅ 执行测试

## 星数曲线

```mermaid
xychart-beta
    title "bobby-sheng/aitestmind 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-24"]
    y-axis "stars" 65 --> 68
    line [66, 67, 67]
```

2026-10-18 66 → 2026-10-24 67（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `47a405b1ac5f` · [字段定义](../../DATASET.md)*
