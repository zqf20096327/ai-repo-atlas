# sodam-ai/GitHub-Explorer

⭐ 15 · TypeScript · MIT · 推送 2026-07-20 · [GitHub](https://github.com/sodam-ai/GitHub-Explorer) · 个人维护 · 中文 README

**自然语言搜索 GitHub 仓库/代码/Issue 的桌面应用，AI 为可选功能**

基于 Tauri + React + TypeScript 的个人用桌面程序：以自然语言搜索 GitHub 仓库、代码与 Issue，支持过滤器、书签收藏、趋势查看、离线缓存检索与集合 JSON 导入导出。核心搜索功能不依赖 AI；AI 仅用于搜索结果摘要与代码 Q&A，可选 OpenAI、Anthropic、Gemini、Groq 或本地 Ollama/LM Studio 六个提供者。数据（搜索历史、API 密钥）仅存本地，密钥经 OS 钥匙串管理，无自有服务器。仓库当前无 LICENSE 文件，自动更新功能未完成，无自动化单元测试。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 存储库/代码/Issue 三类搜索与书签收藏，AI 不可用也可使用
- AI 摘要与代码问答支持 6 个提供者（含本地 Ollama/LM Studio）
- API 密钥存于 OS 钥匙串，数据存本地 SQLite，无自有服务器
- 规则式 README 摘要生成（AI 不需要）

## 适用场景

- 用日常语言查找和筛选 GitHub 开源项目
- 对感兴趣的仓库代码提问并获取 AI 摘要
- 收藏整理仓库到集合并跨设备备份迁移

## 场景标签

`语义搜索` · 领域:知识与检索

## 证据(README 行号)

> L30: - **AI 없이도 핵심 기능 전부 사용 가능**: 저장소 검색, 코드 검색, 이슈 검색, 북마크, 트렌딩 확인은 AI 설정 없이 바로 됩니다.
> L31: - **AI는 선택 사항**: 검색 결과 요약과 "이 코드가 뭐 하는 거야?" 같은 질문(코드 Q&A) 기능만 AI를 씁니다. 원하는 AI 서비스(OpenAI, Anthropic, Google Gemini,

## 星数曲线

```mermaid
xychart-beta
    title "sodam-ai/GitHub-Explorer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `5d0be48dac34` · [字段定义](../../DATASET.md)*
