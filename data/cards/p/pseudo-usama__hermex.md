# pseudo-usama/hermex

⭐ 38 · Python · NOASSERTION · 推送 2026-10-11 · [GitHub](https://github.com/pseudo-usama/hermex) · [官网](https://hermex.usama.ai) · 个人维护

**用 Python 自动化操作 ChatGPT/Gemini 免费网页版的库**

通过 undetected-chromedriver 驱动真实 Chrome 浏览器访问 ChatGPT 与 Gemini 的免费网页界面，自动输入消息、上传附件、等待生成并把回复以 AssistantMessage 数据类（文本与图片路径）返回 Python，无需 API key 或付费。使用持久化浏览器配置文件保持登录会话，首次需运行 setup() 登录；访客模式仅支持基础文本查询，文件上传与图像生成需登录。支持 9 种附件格式、去水印选项与 UI 状态查询。README 声明面向爱好/脚本/研究而非生产环境，且 UI 改版可能导致失效，需遵守平台服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 无 API key，直接驱动网页 UI 获取模型回复
- 附件上传支持 jpg/png/pdf/csv 等 9 种格式
- 持久化浏览器配置文件保持登录会话
- 统一接口封装 Gemini 与 ChatGPT 两个客户端

## 适用场景

- 脚本中偶发调用 LLM 而不想付 API 费用
- 对图片做 OCR 或描述并取回结果
- 自动生成图片并下载到本地目录

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L24: Hermex lets you automate ChatGPT and Gemini with Python — no API keys, no billing, no paywalls. It opens a real Chr
> L33: It uses undetected-chromedriver under the hood to avoid bot detection, and reuses a persistent browser profile so y

## 星数曲线

```mermaid
xychart-beta
    title "pseudo-usama/hermex 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-31"]
    y-axis "stars" 36 --> 39
    line [37, 38, 38]
```

2026-10-18 37 → 2026-10-31 38（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `1e7552d0824e` · [字段定义](../../DATASET.md)*
