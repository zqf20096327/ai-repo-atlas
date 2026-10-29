# hellosunghyun/Startidy

⭐ 69 · TypeScript · 推送 2026-02-03 · [GitHub](https://github.com/hellosunghyun/Startidy) · 个人维护 · 中文 README

**用 Gemini 自动把 GitHub Stars 归类到 Lists 的 CLI 工具**

面向 GitHub 用户的命令行工具：读取用户全部标星仓库，调用 Google Gemini（gemini-2.5-flash）分析标题、描述与 README，规划最多 32 个 `Major: Minor` 层级分类（如 `Lang: Python`），并自动创建 GitHub Lists、把标星仓库批量归类；支持全自动化 run 或 plan/create-lists/classify 分步执行、--dry-run 模拟与 --only-new 增量处理。分类按每批 20 个仓库并行。需配置 GitHub Token 与 Gemini API Key；受 GitHub Lists 上限 32 个、名称 20 字符及 Gemini 免费档 15 请求/分钟限制。npm 全局安装或源码运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Gemini 分析标星仓库并规划最多 32 个层级分类
- 全自动化 run 或 plan/create-lists/classify 分步执行
- 每批 20 仓库并行分类，支持 --dry-run 与 --only-new
- Token/用户名/Gemini Key 可经 CLI 参数、环境变量或 .env 配置

## 适用场景

- 标星仓库积累过多，想自动整理成分类 Lists
- 只增量整理新标星的仓库
- 模拟运行预览分类结果后再正式执行

## 场景标签

`工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: AI-powered CLI tool to automatically organize your GitHub Stars into Lists.
> L11: - **Automatic Category Planning**: Gemini AI analyzes your starred repositories and creates 32 optimal categories
> L217: - **AI**: Google Gemini (gemini-2.5-flash)

## 星数曲线

```mermaid
xychart-beta
    title "hellosunghyun/Startidy 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-29"]
    y-axis "stars" 67 --> 70
    line [68, 69, 69]
```

2026-10-18 68 → 2026-10-29 69（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `1b696a578526` · [字段定义](../../DATASET.md)*
