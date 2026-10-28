# Co-Messi/supercut

⭐ 22 · TypeScript · MIT · 推送 2026-10-10 · [GitHub](https://github.com/Co-Messi/supercut) · [官网](https://supercut-five.vercel.app) · 组织维护

**AI 导演自动拍摄真实 Web 应用并生成产品发布视频的 CLI**

面向开发者的命令行工具：输入运行中的应用 URL，AI 导演读取源码与 DOM、编写拍摄脚本（recipe），由确定性浏览器录制真实操作画面，再渲染为最长 60 秒的带运镜、背景与配乐的 MP4。支持 DeepSeek、OpenRouter 及 OpenAI 兼容自定义 provider，generate 流程需 LLM API key，record/render 两个阶段无需 LLM；也可让 Claude Code 等 coding agent 充当导演实现免 key 路径。各阶段以 JSON 工件交接，事件日志为公开契约。默认排除删除/支付等危险控件，生成前打印动作清单并确认。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 拍摄真实应用：读取源码与 DOM 后由浏览器逐帧录制，不伪造画面
- 五阶段流水线（analyze/script/record/qc/render），各阶段以 JSON 工件交接，可中断改写续跑
- generate 有默认 30 万 token 的 LLM 花费上限，可调可关
- 提供 Claude Code 插件/技能的免 API key 路径

## 适用场景

- 给本地运行的 Web 应用自动生成 60 秒产品发布视频
- 让 coding agent（如 Claude Code）作为导演拍摄并渲染宣传视频
- 通过手写 recipe 与 record/render 无 key 离线录制渲染

## 场景标签

`浏览器自动化` `视频生成` · 领域:效率与自动化

## 证据(README 行号)

> L3:  Point an AI director at your live app. Get a cinematic 60 second launch video.
> L71:  your app URL ──▶ 1 analyze   read the source + crawl the app, pick the money moments (LLM)
> L75:                   5 render    cinematic compositing ──▶ final.mp4 (up to 60s)

## 星数曲线

```mermaid
xychart-beta
    title "Co-Messi/supercut 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 21 --> 23
    line [22, 22]
```

2026-10-18 22 → 2026-10-28 22（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `a400b99860e4` · [字段定义](../../DATASET.md)*
